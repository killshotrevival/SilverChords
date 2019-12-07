from django.shortcuts import render
from .models import notification
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class notificationListView(ListView):
    model = notification
    template_name = 'notification/home.html'
    def get_context_data(self, **kwargs):
        con = notification.objects.filter(owner_id = self.request.user.id).values('user', 'header')
        for c in con:
            username = User.objects.filter(id = c['user']).values('username')
            c['user'] = username[0]['username']
        context = {
            'notifications' : con
        }
        return context
@login_required
def notidata(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        us = User.objects.filter(username=name).values('id')
        id = us[0]['id']
        data = notification.objects.filter(user=id, owner_id=request.user.id).values('contect')
        return HttpResponse(data[0]['contect'])
    else:
        return HttpResponse('Failure')

    
