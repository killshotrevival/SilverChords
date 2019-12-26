import json
from django.shortcuts import render
from .models import notifi
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from beats.models import cart


@method_decorator(login_required, name='dispatch')
class notificationListView(ListView):
    model = notifi
    template_name = 'notifis/home.html'
    def get_context_data(self, **kwargs):
        con = notifi.objects.filter(owner_id = self.request.user.id).values('nid','user', 'header','time', 'n_read','contect').order_by('-time')
        for c in con:
            username = User.objects.filter(id = c['user']).values('username', 'id')
            c['user'] = username[0]['username']
            c['id'] = username[0]['id']
        count=0
        c2 = cart.objects.filter(user_id=self.request.user.id)
        nc = notifi.objects.filter(owner_id=self.request.user.id)
        for i in c2:
            count = count+i.itemcount
        context = {
            'notifications' : con, 
            'count':count,
            'ncount': nc.count()
        }
        return context

def delete(request,pk):
    count=0
    c2 = cart.objects.filter(user_id=request.user.id)
    nc = notifi.objects.filter(owner_id=request.user.id)
    for i in c2:
        count = count+i.itemcount
    notifi.objects.filter(nid=pk).delete()
    con = notifi.objects.filter(owner_id = request.user.id).values('nid','user', 'header','time', 'n_read','contect').order_by('-time')
    for c in con:
        username = User.objects.filter(id = c['user']).values('username', 'id')
        c['user'] = username[0]['username']
        c['id'] = username[0]['id']
    return render(request, 'notifis/home.html', {'notifications' : con, 'count': count, 'ncount':nc.count()})

    
