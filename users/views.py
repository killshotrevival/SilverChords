from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerform, InfoUpdateForm, BeatUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from .models import quote, helpinfo, verification, profile, advice
from django.contrib.auth import logout, login
from django.views.generic import DetailView
from django.contrib.auth.models import User
from beats.models import work_info, cart
from notifis.models import notifi
from .forms import NotifyForm, helpform, verifiform, adviceform


def register(request):
    if request.method=='POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username)
            login(request, user[0])
            messages.success(request, f'Account Created for {username}!')
            messages.success(request, 'Go to the Edit Info Page and Update your details :)')
            return redirect('home')
        else:
            error = form.errors
            return render(request, 'users/register.html', {'form': form, 'error': error})
    else:
        form = registerform()
        return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    nc = notifi.objects.filter(owner_id=request.user.id)
    beats = work_info.objects.filter(user_id=request.user.id)
    veri = profile.objects.filter(user_id=request.user.id).values('verified', 'veri_submit')
    if( not veri[0]['verified']):
        if(not veri[0]['veri_submit']):
            messages.success(request, 'Please verifi your details to obtain the maximum of our services')
    return render(request, 'users/profile.html', {'beats': beats, 'count':count, 'ncount':nc.count()})

@login_required
def edit(request):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    if request.method=='POST':
        form1 = InfoUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid():
            form1.save()
            return redirect('profile')
        else:
            messages.warning(request, 'Some errors in the input, please try again..')
            return render(request, 'users/profile.html', {'count':count, 'ncount':nc.count()})
    else:
        form = InfoUpdateForm(instance=request.user.profile)
        return render(request, 'users/editinfo.html', {'form': form, 'count':count, 'ncount':nc.count()})


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html')

def galleryouter(request):
    return render(request, 'beats/gallery_outer.html')

@method_decorator(login_required, name='dispatch')
class UserDetailsView(DetailView):
    model = User
    template_name = 'users/infouser.html'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["beats"] = work_info.objects.filter(user_id=pk)
        count=0
        c2 = cart.objects.filter(user_id=self.request.user.id)
        nc = notifi.objects.filter(owner_id=self.request.user.id)
        for i in c2:
            count = count+i.itemcount
        context["count"] = count
        context['ncount'] = nc.count()
        return context

@login_required
def notif(request,pk):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('data')
            header1 = form.cleaned_data.get('hae')
            user = User.objects.filter(id=pk).first()
            beats = work_info.objects.filter(user_id=pk)
            noti = notifi(user_id=request.user.id, owner_id=user, header=header1, contect=data)
            noti.save()
            messages.add_message(request, messages.SUCCESS, 'Message Sent')
            return render(request, 'users/infouser.html', {'user':user,'beats':beats, 'count':count, 'ncount':nc.count()})
        else:
           messages.add_message(request, messages.WARNING, 'Error occuried, please try again later')
           user = User.objects.filter(id=pk).first()
           return render(request, 'users/infouser.html', {'user':user, 'count':count, 'ncount':nc.count()})
    else:
        messages.add_message(request, messages.ERROR, 'Error occuried, please try again later')
        user = User.objects.filter(id=pk).first()
        return render(request, 'users/infouser.html', {'user':user, 'count':count, 'ncount':nc.count()})

def helpinfofun(request):
    if request.method =="POST":
        form = helpform(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            hi = helpinfo(name=name, email=email, message=message)
            hi.save()
            messages.add_message(request, messages.SUCCESS, 'Message Sent')
            return render(request, 'beats/silverchords.html')

        else:
            return render(request, 'beats/silverchords.html')
    else:
        return render(request, 'beats/silverchords.html')
@login_required
def verifi(request):
    nc = notifi.objects.filter(owner_id=request.user.id)
    if(not request.user.profile.veri_submit):
        if request.method=="POST":
            form = verifiform(request.POST)
            if form.is_valid():
                phone = form.cleaned_data.get('phone')
                email = form.cleaned_data.get('email')
                vtype = form.cleaned_data.get('vtype')
                vno = form.cleaned_data.get('vno')
                veri = verification(user_id=request.user.id, phone=phone, email=email, vtype=vtype, vno=vno)
                veri.save()
                request.user.profile.verichange()
                return render(request, 'users/verification_done.html')
            else:
                messages.add_message(request, messages.WARNING, 'Some error occuried during uploading your details, please try after some time.')
                form = verifiform()
                return render(request, 'users/verification.html', {'form':form, 'ncount':nc.count()})

        else:
            form = verifiform()
            return render(request, 'users/verification.html', {'form':form, 'ncount':nc.count()})
    else:
        return render(request, 'users/verification_done.html', {'ncount':nc.count()})

@login_required
def advice_view(request):
    if request.method=='POST':
        form = adviceform(request.POST)
        if form.is_valid():
            platform = form.cleaned_data.get('platform')
            content = form.cleaned_data.get('content')
            ad = advice(user_id=request.user.id, platform=platform, content=content)
            ad.save()
            messages.success(request, "Your request has been posted successfully, we will get back to you soon. Don't forget to check your notification box regulary. We will do our best to help you ")
            return render(request, 'users/advice.html')
        else:
            messages.warning(request, 'Some problem occuried while, uploading your form, please try again.')
            return render(request, 'users/advice.html')
    else:
        return render(request, 'users/advice.html')
@login_required
def deleteb(request, pk):
    work_info.objects.filter(Bid=pk).delete()
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    nc = notifi.objects.filter(owner_id=request.user.id)
    beats = work_info.objects.filter(user_id=request.user.id)
    veri = profile.objects.filter(user_id=request.user.id).values('verified', 'veri_submit')
    if( not veri[0]['verified']):
        if(not veri[0]['veri_submit']):
            messages.success(request, 'Please verifi your details to obtain the maximum of our services')
    return render(request, 'users/profile.html', {'beats': beats, 'count':count, 'ncount':nc.count()})

def alllogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

@login_required
def editb(request, pk):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    if request.method=='POST':
        form1 = BeatUpdateForm(request.POST, request.FILES)
        if form1.is_valid():
            w = work_info.objects.filter(Bid=pk)
            name = form1.cleaned_data.get('beat_name')
            w[0].editn(name)
            genre = form1.cleaned_data.get('genre')
            w[0].editg(genre)
            desc = form1.cleaned_data.get('beat_desc')
            w[0].editd(desc)
            price = form1.cleaned_data.get('price')
            w[0].editp(price)
            return redirect('profile')
        else:
            messages.warning(request, 'Some errors in the input, please try again..')
            return render(request, 'users/profile.html', {'count':count, 'ncount':nc.count()})
    else:
        w = work_info.objects.filter(Bid=pk)
        return render(request, 'beats/editbeatinfo.html', {'count':count, 'ncount':nc.count(), 'Bid': w[0].Bid, 'price':w[0].price})