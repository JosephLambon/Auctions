from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("choices/", views.choices, name="choices"),
    path("<int:listing_id>/", views.listing, name="listing"),
    path("category/<str:category>/", views.category, name="category"),
    path("comment/<int:listing_id>/<int:user_id>/", views.comment, name="comment"),
    path("create/<int:user_id>/", views.create_listing, name="create"),
    path("close/<int:listing_id>/<int:user_id>/", views.close, name="close"),
    path("wishlist/<int:user_id>/", views.wish_view, name="wish_view"),
    path("wishlist/add/<int:listing_id>/<int:user_id>", views.add_wishlist, name="add_wishlist"),
    path("bid/<int:listing_id>/<int:user_id>", views.bid, name="bid"),
    path("wishlist/remove/<int:listing_id>/<int:user_id>", views.rem_wishlist, name="rem_wishlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
