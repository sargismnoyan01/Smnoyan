# Generated by Django 5.1.4 on 2024-12-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_about_dt_end_alter_about_dt_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='present',
            field=models.CharField(blank=True, max_length=255, verbose_name='Present'),
        ),
        migrations.AlterField(
            model_name='about',
            name='dt_end',
            field=models.DateField(blank=True, null=True, verbose_name='Date end'),
        ),
    ]
