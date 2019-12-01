from django.shortcuts import render
from .models import notification
from django.views.generic import ListView

class notificationListView(ListView):
    model = notification
    template_name = 'notification/home.html'
    def get_context_data(self, **kwargs):
        con = notification.objects.filter(user_id = self.request.user.id)
        context = {
            'notifications' : con
        }
        return context
    
