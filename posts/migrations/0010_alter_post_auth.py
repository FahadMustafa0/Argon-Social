# Generated by Django 3.2.9 on 2021-12-07 05:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='auth',
            field=models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User),
        ),
    ]
