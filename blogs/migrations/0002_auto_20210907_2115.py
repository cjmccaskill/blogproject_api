# Generated by Django 3.2.7 on 2021-09-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
