# Generated by Django 3.0.3 on 2021-01-16 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210116_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
