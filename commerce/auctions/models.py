from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.db import models

# Fashion, Toys, Electronics, Home,
CATEGORY_CHOICES = (
    ('Fashion', 'FASHION'),
    ('Toys', 'TOYS'),
    ('Electronics', 'ELECTRONICS'),
    ('Home', 'HOME')
)

class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    wishlist = models.ManyToManyField('Listing', related_name='users_wishlist')

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    current_bid = models.DecimalField(decimal_places=2, max_digits=10)
    bidder = models.ManyToManyField(User, related_name='bidder_listings', blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_listings', blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    img_url = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)

class Bid(models.Model):
    new_bid = models.DecimalField(decimal_places=2, max_digits=10,
                                  blank=True, null=True)

class Comment(models.Model):
    comment = models.CharField(max_length=200,
                               blank=True, null=True)
    title = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, related_name='listing_titles', blank=False)
    commentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_commented', blank=False)
