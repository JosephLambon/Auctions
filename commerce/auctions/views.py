from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Listing, Comment, Bid, User, CATEGORY_CHOICES

from django import forms

class BidForm(forms.Form):
    new_bid = forms.DecimalField(decimal_places=2, max_digits=10, min_value=0)

class ListingForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=200)
    current_bid = forms.DecimalField(decimal_places=2, max_digits=10)
    bidder = forms.CharField(max_length=200, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    img_url = forms.CharField(max_length=1000)

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=200, required=False)

def index(request):
    list = Listing.objects.all()
    active_listings = [listing for listing in list if listing.active]
    return render(request, "auctions/index.html", {
            "listings": active_listings
    })

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    all_comments = Comment.objects.all()
    comments =  [comment for comment in all_comments if comment.title.title == listing.title]
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": comments,
        "form": BidForm(),
        "comment_form": CommentForm()
        })

def category(request, category):
    listings = Listing.objects.all()
    category = category.split("'")
    category = category[1]
    category_listings = [listing for listing in listings if listing.category==category]
    a_category_listings = [listing for listing in category_listings if listing.active]
    if a_category_listings==[]:
        return render(request, "auctions/index.html", {
            "listings": a_category_listings,
            "title": category,
            "message": "There are no current listings in this category.",
            "color": "red"
            })
    return render(request, "auctions/index.html", {
            "listings": a_category_listings,
            "title": category
            })

def choices(request):
    return render(request, "auctions/choices.html", {
        "choices": CATEGORY_CHOICES
    })

@login_required
def comment(request, listing_id, user_id):
    user = User.objects.get(id=user_id)
    listing = Listing.objects.get(id=listing_id)
    if request.method=="POST":
        # Read form data
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data["comment"]
            # Set comment parameters as form parameters
            comment = Comment(commentor=user,
                              title=listing,
                              comment=new_comment)
            # Save and render listing page.
            comment.save()
            all_comments = Comment.objects.all()
            comments =  [comment for comment in all_comments if comment.title.title == listing.title]
            print(all_comments)
            print("Added:", new_comment)
            return render(request, "auctions/listing.html", {
                    "listing": listing,
                    "comments": comments,
                    "form": BidForm(),
                    "comment_form": CommentForm()
                    })
    all_comments = Comment.objects.all()
    comments =  [comment for comment in all_comments if comment.title.title == listing.title]
    print(all_comments)
    print("No comment added.")
    return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "Error: Unable to add comment",
                "color:": "red",
                "comments": comments,
                "form": BidForm(),
                "comment_form": CommentForm()
                })
    

@login_required
def create_listing(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method=="POST":
        # Read form data
        form = ListingForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title"]
            new_description = form.cleaned_data["description"]
            new_current_bid = form.cleaned_data["current_bid"]
            new_category = form.cleaned_data["category"]
            new_img_url = form.cleaned_data["img_url"]
        # Create listing
        # Set listing parameters as form parameters
            listing = Listing(title=new_title,
                        description=new_description,
                        current_bid=new_current_bid,
                        creator=user,
                        category=new_category,
                        img_url=new_img_url)
            # Save and render listing page.
            listing.save()
        return render(request, "auctions/listing.html", {
                            "listing": listing,
                            "form": BidForm(),
                            "comment_form": CommentForm(),
                            "message": "Listing created succesfully.",
                            "color": "green"
                        })
    else:
        # Load page and pass in ListingForm()
        return render(request, "auctions/create.html", {
            "form": ListingForm(),
            "user": user
        })

@login_required
def close(request, listing_id,  user_id):
    if request.method == "POST":
        wish = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        wish.active = False
        wish.save()
        return render(request, "auctions/listing.html", {
                            "listing": wish,
                            "form": BidForm(),
                            "comment_form": CommentForm(),
                            "message": "Listing auction closed.",
                            "color": "green"
                        })

@login_required
def add_wishlist(request, listing_id, user_id):
    # Add item to user's wishlist
    if request.method == "POST":
        wish = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        for item in user.wishlist.all():
            if wish.id == item.id:
                return render(request, "auctions/listing.html", {
                    "listing": wish,
                    "form": BidForm(),
                    "comment_form": CommentForm(),
                    "message": "Item already on your wishlist.",
                    "color": "red"
                })

        user.wishlist.add(wish)
        return render(request, "auctions/listing.html", {
            "listing": wish,
            "form": BidForm(),
            "comment_form": CommentForm(),
            "message": "Item added to your wishlist.",
            "color": "green"
        })
        
    # Handle non-POST requests or other cases
    return HttpResponse("Invalid request")

@login_required
def rem_wishlist(request, listing_id, user_id):
     #Remove item from user's wishlist
    if request.method == "POST":
        wish = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        list = user.wishlist.all()
        for item in user.wishlist.all():
            if wish.id != item.id:
                continue
            elif wish.id == item.id:
                user.wishlist.remove(wish)
                list = user.wishlist.all()
                return render(request, "auctions/wishlist.html", {
                    "wishlist": list,
                    "message": "Item removed from your wishlist.",
                    "user": user,
                    "color": "green"
                })
        return render(request, "auctions/wishlist.html", {
                    "wishlist": list,
                    "message": "Item not found in your wishlist.",
                    "user": user,
                    "color": "red"
                })

@login_required
def wish_view(request, user_id):
    user = User.objects.get(id=user_id)
    list = user.wishlist.all()
    active_listings = [listing for listing in list if listing.active]
    return render(request, "auctions/wishlist.html", {
        "wishlist": active_listings,
        "user": user
    })

@login_required
def bid(request, listing_id, user_id):
    if request.method == "POST":
        wish = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid = form.cleaned_data["new_bid"]
            if new_bid > wish.current_bid:
                wish.current_bid =  new_bid
                wish.bidder.clear()  # Clear the previous bidders (if any)
                wish.bidder.add(user)
                wish.save()
                return render(request, "auctions/listing.html", {
                        "listing": wish,
                        "form": BidForm(),
                        "comment_form": CommentForm(),
                        "message": "Bid made successfully.",
                        "color": "green"
                    })
            elif new_bid <= wish.current_bid:
                return render(request, "auctions/listing.html", {
                    "listing": wish,
                    "form": BidForm(),
                    "comment_form": CommentForm(),
                    "message": "Bid must be greater than current bid.",
                    "color": "red"
                    })
        else:
            return render(request, "auctions/listing.html", {
                    "listing": wish,
                    "form": BidForm(),
                    "comment_form": CommentForm(),
                    "message": "Error: Enter a valid bid",
                    "color": "red"
                })
        

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
