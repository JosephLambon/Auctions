This demo auction site was my first Django project, completed as a Coursework within Harvard University's CS50W course.
On this site, there is the functionality to register a user account, add listings, add/view your wishlist,
as well as bid and comment on other listings.

Depending on whether you're the one who has listed an item, is bidding on an item, or has won a closed auction, the displayed pages will differ.
Register one or two accounts and this should be seen.

Functionality can be seen here: https://youtu.be/dPfLyy0nitk

To run, you’ll need to: 
Set-up a virtual environment (virtualenv).
Install python to your environment
Install django to your environment

Run the following commands:
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
