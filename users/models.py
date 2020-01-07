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
    verified = models.BooleanField(default=False)
    veri_submit = models.BooleanField(default=False)


    def verichange(self):
        self.veri_submit=True
        self.save()

    def __str__(self):
        return f'{self.user.username} Profile'


class quote(models.Model):
    Qid = models.AutoField(primary_key=True)
    data = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.Qid} quote'

class verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, default='000000000000', unique=True)
    email = models.EmailField(unique=True, default='silever@chords.com')
    vtype = models.CharField(max_length=200, default='vtype')
    vno = models.CharField(max_length=100, default='0000000000')
    front_photo = models.ImageField( default='ap_default.jpg', upload_to='verifi_front')
    back_photo = models.ImageField( default='ap_default.jpg', upload_to='verifi_back')

    def __str__(self):
        return f'{self.user.username} Verification'


class helpinfo(models.Model):
    help_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class advice(models.Model):
    a_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(default='U', max_length=20,choices=[
        ('Y','Youtube'),
        ('I','Instagram'),
        ('F','Facebook'),
        ('S','Snapchat'),
        ('U', 'Us')
        ])
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} form'
    
    