# Generated by Django 4.2.6 on 2023-11-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_starting_bid_listing_current_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bidder',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
