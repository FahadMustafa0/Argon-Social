# Generated by Django 3.2.9 on 2021-12-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_followers'),
        ('posts', '0020_post_author1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author1',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
