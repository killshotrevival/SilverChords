from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    artist_photo = models.ImageField(default='ap_default.jpg', upload_to='artist_photo')
    cover_photo = models.ImageField(default='cp_default.jpg', upload_to='cover_photo')
    place = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000)
    badge = models.CharField(max_length=20)
    fb = models.CharField(default='facebook.com', max_length=100)
    insta = models.CharField(max_length=100, default='instagram.com')
    youtube = models.CharField(max_length=100, default='youtube.com')
    hashtags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class quote(models.Model):
    Qid = models.AutoField(primary_key=True)
    data = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.Qid} quote'


class verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    vtype = models.CharField(max_length=200)
    vno = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Verification'