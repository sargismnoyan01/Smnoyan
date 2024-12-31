# Generated by Django 5.1.4 on 2024-12-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_sendmessage_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendmessage',
            options={'verbose_name': 'Messages', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AddField(
            model_name='maininformations',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
    ]