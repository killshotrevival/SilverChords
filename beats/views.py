from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import beatupload, searchform, reviewsform
from .models import work_info, reviews, Userhistory, cart
from users.models import quote, profile, verification
from django import forms
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from notifis.models import notifi



@login_required
def home(request):
    quotea=quote.objects.order_by("?").first()
    ver = profile.objects.filter(user_id=request.user.id).values('verified', 'veri_submit')
    if( not ver[0]['verified']):
        if(not ver[0]['veri_submit']):
            messages.warning(request, 'Please verifi your details to obtain the maximum of our services')
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    ################################
    mt = work_info.objects.all().order_by('-listens')[:10]
    ff = work_info.objects.all().order_by('-beat_date')[:10]
    hist = Userhistory.objects.filter(user_id=request.user.id).order_by('-h_id')
    if hist.count()==0:
        fu = work_info.objects.filter(genre='rock')
        return render(request, 'beats/silverchords_home.html', {'quote':quotea, 'count':count, 'ncount':nc.count(), 'mt':mt, 'ff':ff, 'fu':fu})
    else:
        g = hist[0].Bid.genre
        fu = work_info.objects.filter(genre=g)
        return render(request, 'beats/silverchords_home.html', {'quote':quotea, 'count':count, 'ncount':nc.count(), 'mt':mt, 'ff':ff, 'fu':fu})



def silverchords(request):
    return render(request, 'beats/silverchords.html')


def gallery(request):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    return render(request, 'beats/gallery.html', {'count':count, 'ncount':nc.count()})


@login_required
def search(request):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    if request.method=='POST':
        form = searchform(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search_token')
            work = work_info.objects.filter(beat_name__contains=search)
            genres = work_info.objects.filter(genre__contains=search)
            user = User.objects.filter(username__contains=search)
            count=0
            c2 = cart.objects.filter(user_id=request.user.id)
            for i in c2:
                count = count+i.itemcount
            return render(request, 'beats/search.html', {'work':work, 'genres':genres, 'users':user, 'name':search, 'count':count, 'ncount':nc.count()})
        quotea=quote.objects.order_by("?").first()
        return render(request, 'beats/silverchords_home.html.', {'quote':quotea, 'count':count, 'ncount':nc.count()})
    else:
        quotea=quote.objects.order_by("?").first()
        return render(request, 'beats/silverchords_home.html.', {'quote':quotea, 'count':count, 'ncount':nc.count()})

@login_required
def listensupdate(request,pk):
    query = work_info.objects.filter(Bid=pk)
    query.listens_update()
    
@login_required
def playsonng(request):
    if request.method =='POST':
        id = request.POST.get('Bid')
        work = work_info.objects.filter(Bid = id)
        work[0].listens_update()
        his1 = Userhistory.objects.filter(user_id=request.user.id, Bid=id)
        if (his1.count()==0):
            his2 = Userhistory.objects.filter(user_id=request.user.id)
            if (his2.count()<10):
                us = Userhistory(user_id=request.user.id, Bid=work[0])
                us.save()
            else:
                did=his2[0].retBid()
                Userhistory.objects.filter(user_id=request.user.id, Bid=did).delete()
                us1 = Userhistory(user_id=request.user.id, Bid=work[0])
                us1.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Failure")

@login_required
def historydetail(request,pk):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    work = work_info.objects.filter(Bid = pk).order_by('-h_id')
    return render(request, 'beats/beatdetails.html', {'beat':work[0], 'count':count, 'ncount':nc.count()})

@login_required
def upload(request):
    if request.method=='POST':
        form1 = beatupload(request.POST, request.FILES)
        if form1.is_valid():
            user1 = form1.save(commit=False)
            user1.user_id = request.user.id
            user1.producer = request.user.username
            user1.save()
            return redirect('home')
        else:
            count=0
            c2 = cart.objects.filter(user_id=request.user.id)
            nc = notifi.objects.filter(owner_id=request.user.id)
            for i in c2:
                count = count+i.itemcount
            messages.warning(request, 'Not a valid input, please try again..')
            return render(request, 'beats/upload.html', {'count':count, 'ncount':nc.count()})
    else:
        count=0
        c2 = cart.objects.filter(user_id=request.user.id)
        nc = notifi.objects.filter(owner_id=request.user.id)
        for i in c2:
            count = count+i.itemcount
        form1 = beatupload()
        return render(request, 'beats/upload.html', {'count':count, 'ncount':nc.count(), 'form':form1})

@method_decorator(login_required, name='dispatch')
class BeatListView(ListView):
    model = work_info
    template_name = 'beats/beatlist.html'
    #queryset = work_info.objects.filter(genre='rock')
    context_object_name = 'beats'
    ordering = ['-beat_date']
    paginate_by = 3

@method_decorator(login_required, name='dispatch')
class HistoryNameList(ListView):
    model = Userhistory
    #context_object_name = 'historys'
    template_name='beats/history.html'
    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        con = Userhistory.objects.filter(user_id=self.request.user.id).order_by('-h_id')
        count=0
        c2 = cart.objects.filter(user_id=self.request.user.id)
        nc = notifi.objects.filter(owner_id=self.request.user.id)
        for i in c2:
            count = count+i.itemcount
        context = {
        
            'historys':con,
            'count':count,
            'ncount':nc.count()
        }
        return context

@login_required
def beatdetails(request, pk):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    if request.method=='POST':
        form = reviewsform(request.POST)
        if form.is_valid():
            rate = form.cleaned_data.get('rating')
            cmnt = form.cleaned_data.get('comment')
            us = work_info.objects.filter(Bid=pk)
            riv = reviews(Bid=us[0], user_id=request.user.id, rating=rate, comment=cmnt)
            riv.save()
            messages.success(request, 'Your review is succesfully posted!!!')
            rev = reviews.objects.filter(Bid=pk).order_by('-review_id')
            beat = work_info.objects.filter(Bid=pk)
            form1 = reviewsform()
            return render(request, 'beats/beatdetails.html', {'reviews':rev, 'beat':beat[0], 'form':form1, 'count':count, 'ncount':nc.count()})
        else:
            messages.warning(request, 'Some Error occuried while posting your review, please try again later.')
            rev = reviews.objects.filter(Bid=pk).order_by('-review_id')
            beat = work_info.objects.filter(Bid=pk)
            form1 = reviewsform()
            return render(request, 'beats/beatdetails.html', {'reviews':rev, 'beat':beat[0], 'form':form1, 'count':count, 'ncount':nc.count()})
    else:
        rev = reviews.objects.filter(Bid=pk).order_by('-review_id')
        beat = work_info.objects.filter(Bid=pk)
        form1 = reviewsform()
        return render(request, 'beats/beatdetails.html', {'reviews':rev, 'beat':beat[0], 'form':form1, 'count':count, 'ncount':nc.count()})

    
@login_required
def beatcart(request,pk):
    w = work_info.objects.filter(Bid=pk)
    p = w[0].price
    c1 = cart.objects.filter(user_id=request.user.id, Bid=pk)
    if(c1.count()>0):
        c1[0].coutninc()
    else:
        c =cart(user_id=request.user.id, Bid=w[0], price=p)
        c.coutninc()
        c.save()
    form1 = reviewsform()
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    rev = reviews.objects.filter(Bid=pk).order_by('-review_id')
    return render(request, 'beats/beatdetails.html', {'reviews':rev, 'beat':w[0], 'form':form1, 'count':count, 'ncount':nc.count()})

