# Generated by Django 3.0.3 on 2021-01-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210117_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='timefield',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
