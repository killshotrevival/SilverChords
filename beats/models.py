from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

class work_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bid = models.AutoField(primary_key=True)
    producer = models.CharField(max_length=100)
    beat_name = models.CharField(max_length=100)
    beat = models.FileField(upload_to='beats')
    genre = models.CharField(max_length=30)
    beat_img = models.ImageField(upload_to='beat_img')
    beat_desc = models.TextField(max_length=2000)
    beat_date = models.DateTimeField(auto_now_add=True)
    listens = models.IntegerField(default=0)

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

