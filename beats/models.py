from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

class work_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bid = models.AutoField(primary_key=True)
    producer = models.CharField(max_length=100)
    beat_name = models.CharField(max_length=100)
    beat = models.FileField(upload_to='beats')
    genre = models.CharField(max_length=30,default='R',choices=[
        ('R','Rock'),
        ('E','Electric'),
        ('Hh','Hip Hop'),
        ('C','Country'),
        ('t', 'Techno/trance'),
        ('Db', 'Drum And Bass'),
        ])
    beat_img = models.ImageField(upload_to='beat_img')
    beat_desc = models.TextField(max_length=2000)
    beat_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)
    listens = models.IntegerField(default=0)

    def editp(self, var1):
        self.price = var1
        self.save()

    def editn(self, var1):
        self.beat_name = var1
        self.save()

    def editd(self, var1):
        self.beat_desc = var1
        self.save()
    
    def editg(self, var1):
        self.genre = var1
        self.save()

    def __str__(self):
        return self.beat_name
    
    def listens_update(self):
        self.listens=self.listens+1
        self.save()
        

class reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    Bid = models.ForeignKey(work_info, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5,choices=[
        (1,'Poor'),
        (2,'Ok Ok'),
        (3,'Average'),
        (4,'Great'),
        (5, 'Blast'),
        ])
    comment = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.user.username} review for {self.Bid.beat_name}'

class Userhistory(models.Model):
    h_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bid = models.ForeignKey(work_info, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.Bid.beat_name}'

    def retBid(self):
        return f'{self.Bid.Bid}'

class cart(models.Model):
    cid =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bid = models.ForeignKey(work_info, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    itemcount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} cart has {self.Bid.beat_name} {self.itemcount}'

    def coutninc(self, v1):
        self.itemcount = self.itemcount+v1
        self.save()  

class bought(models.Model):
    bbid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_name = models.CharField(max_length=100)
    b_img = models.ImageField(upload_to='bb_img')

    def __str__(self):
        return f'{self.user.username} bought {self.b_name}'