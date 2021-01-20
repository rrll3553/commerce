# Generated by Django 3.0.3 on 2021-01-16 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='time',
            new_name='datefield',
        ),
        migrations.AddField(
            model_name='bid',
            name='timefield',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
