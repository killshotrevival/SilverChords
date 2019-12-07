from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerform, InfoUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from .models import quote
from django.contrib.auth import logout
from django.views.generic import DetailView
from django.contrib.auth.models import User
from beats.models import work_info
from notification.models import notification
from .forms import NotifyForm


def register(request):
    if request.method=='POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')
        else:
            error = form.errors
            return render(request, 'users/register.html', {'form': form, 'error': error})
    else:
        form = registerform()
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    beats = work_info.objects.filter(user_id=request.user.id)
    return render(request, 'users/profile.html', {'beats': beats})

@login_required
def edit(request):
    if request.method=='POST':
        form1 = InfoUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid():
            form1.save()
            return redirect('profile')
        else:
            raise forms.ValidationError('Not a valid input')
    else:
        form = InfoUpdateForm(instance=request.user.profile)
        return render(request, 'users/editinfo.html', {'form': form})


def logout_view(request):
    logout(request)
    quotea=quote.objects.order_by("?").first()
    return render(request, 'users/logout.html', {'quote':quotea})

@method_decorator(login_required, name='dispatch')
class UserDetailsView(DetailView):
    model = User
    template_name = 'users/infouser.html'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["beats"] = work_info.objects.filter(user_id=pk)
        return context

@login_required
def notifi(request,pk):
    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('data')
            header1 = form.cleaned_data.get('header')
            user = User.objects.filter(id=pk).first()
            noti = notification(user_id=request.user.id, owner_id=user, header=header1, contect=data)
            noti.save()
            return render(request, 'notification/confirm.html')

