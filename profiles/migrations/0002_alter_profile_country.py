# Generated by Django 3.2.9 on 2021-12-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
