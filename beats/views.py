import json
from django.shortcuts import render, redirect
from .forms import beatupload
from .models import work_info, reviews, Userhistory
from users.models import quote, profile
from django import forms
from django.views.generic import ListView, DetailView
from .forms import searchform
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def home(request):
    quotea=quote.objects.order_by("?").first()
    return render(request, 'beats/silverchords_home.html.', {'quote':quotea})

@login_required    
def silverchords(request):
    return render(request, 'beats/silverchords.html')

@login_required
def search(request):
    if request.method=='POST':
        form = searchform(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search_token')
            work = work_info.objects.filter(beat_name__contains=search)
            genres = work_info.objects.filter(genre__contains=search)
            user = User.objects.filter(username__contains=search)
            return render(request, 'beats/search.html', {'work':work, 'genres':genres, 'users':user, 'name':search})
    else:
        return render(request, 'beats/base.html')

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
        return HttpResponse("Success")
    else:
        return HttpResponse("Failure")

@login_required
def historydetail(request,pk):
        #id = request.POST.get('Bid')
        work = work_info.objects.filter(Bid = pk)
        return render(request, 'beats/beatdetails.html', {'beat':work[0]})

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
            raise forms.ValidationError('Not a Valid Input')
    else:
       # form = beatupload()
        return render(request, 'beats/upload.html')

@method_decorator(login_required, name='dispatch')
class BeatListView(ListView):
    model = work_info
    template_name = 'beats/beatlist.html'
    #queryset = work_info.objects.filter(genre='rock')
    context_object_name = 'beats'
    ordering = ['-beat_date']
    paginate_by = 3

@method_decorator(login_required, name='dispatch')
class BeatDetailsView(DetailView):
    model = work_info
    template_name = 'beats/beatdetails.html'
    context_object_name = 'beat'
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["reviews"] = reviews.objects.filter(Bid=pk)
        return context

@method_decorator(login_required, name='dispatch')
class HistoryNameList(ListView):
    model = Userhistory
    #context_object_name = 'historys'
    template_name='beats/history.html'
    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        con = Userhistory.objects.filter(user_id=self.request.user.id)
        context = {
        
            'historys':con
        }
        return context
    
    


