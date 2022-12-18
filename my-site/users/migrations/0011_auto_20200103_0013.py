# Generated by Django 2.2.6 on 2020-01-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200103_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='platform',
            field=models.CharField(choices=[('Y', 'Youtube'), ('I', 'Instagram'), ('F', 'Facebook'), ('S', 'Snapchat'), ('U', 'Us')], default='U', max_length=20),
        ),
    ]