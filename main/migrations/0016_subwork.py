# Generated by Django 5.1.4 on 2024-12-30 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_comp_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos', verbose_name='Video')),
                ('many_about', models.TextField(verbose_name='About Text')),
                ('main_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_works', to='main.comp_works')),
            ],
        ),
    ]
