from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerform, InfoUpdateForm
from django.contrib.auth.decorators import login_required
from django import forms



def register(request):
    if request.method=='POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')

    else:
        form = registerform()
        return render(request, 'users/register.html', {'form': form})
        

@login_required
def profile(request):
    return render(request, 'users/profile.html')

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
