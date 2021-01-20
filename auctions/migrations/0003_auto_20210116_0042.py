# Generated by Django 3.0.3 on 2021-01-16 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_listings_bids_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.DeleteModel(
            name='Auction_Listings',
        ),
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Bid'),
        ),
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Comment'),
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
