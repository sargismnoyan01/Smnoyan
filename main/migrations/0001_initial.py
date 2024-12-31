# Generated by Django 5.1.4 on 2024-12-29 11:32

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255, verbose_name='Site name')),
                ('site_owner', models.CharField(max_length=255, verbose_name='Site owner')),
                ('img', models.ImageField(upload_to='owner_first_image', verbose_name='Image')),
                ('profile', models.CharField(max_length=255, verbose_name='Profile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Main Info',
                'verbose_name_plural': 'Main Infos',
            },
        ),
    ]
