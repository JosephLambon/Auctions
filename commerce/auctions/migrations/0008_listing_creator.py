# Generated by Django 4.2.6 on 2023-11-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='creator',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]