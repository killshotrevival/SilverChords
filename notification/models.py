#user_id is the id of the reciever 
#owner_id is the id of sender

from django.db import models
from django.contrib.auth.models import User

class notification(models.Model):
    nid = models.AutoField(primary_key=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name='custom_user_profile')
    time = models.DateTimeField(auto_now_add=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ind_provider_profile')
    n_read = models.BinaryField(default=False)
    header = models.CharField(max_length=200)
    contect = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.user.username} sends {self.owner_id.username}'
