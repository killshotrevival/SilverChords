# Generated by Django 2.2.6 on 2019-12-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191218_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verification',
            name='verified',
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]