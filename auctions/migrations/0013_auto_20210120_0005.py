# Generated by Django 3.0.3 on 2021-01-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('NONE', 'Not applicable'), ('CAR', 'Automobile'), ('BOOK', 'Book'), ('EXERCISE', 'Exercise'), ('FOOD', 'Food'), ('HOME', 'Home'), ('WORK', 'Work')], default='NONE', max_length=64),
        ),
    ]
