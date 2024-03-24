# Auction - Commerce Site
>### A CS50W project

## Contents
1. [Project Synopsis](#project_synopsis)
2. [Project Resources](#project_resources)
3. [Setup and Usage](#setup)
4. [Video Demo](#video)


## <a id='project_synopsis'> Project Synopsis </a>
The aim of this project was to design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

This demo auction site was my first Django project, completed as a Coursework within Harvard University's CS50W course. On this site, there is the functionality to register a user account, add listings, add/view your wishlist, as well as bid and comment on other listings.

Depending on whether you're the one who has listed an item, is bidding on an item, or has won a closed auction, the displayed pages will differ. Register one or two accounts to see this, or watch the video demo below.

## <a id='project_resources'> Project Resources </a>
* [Django](https://www.djangoproject.com/)
> Django is a high-level open source Python framework that makes it easier to build secure web applications.

* [Bootstrap](https://getbootstrap.com/)
> Bootstrap is a front-end library, offering pre-built components and JavaScript plug-ins.

* [SQLite](https://www.sqlite.org/)
> SQLite is a C-language library that implements a fast & reliable SQL database engine.

## <a id='setup'> Setup and Usage </a>
#### [NOTE: Any lines of code included are intended for the command line]

### 1. Install prerequisites
a. Install [Python](https://www.python.org/) </br>
b. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
``` 
 pip install virtualenv
```
### 2. Setup virtual environment
* Create virtual environment </br>
```
# Run this line on the command line
# Replace 'env_name' with whatever your desired env's name is.

virtualenv env_name
```
* Start virtual environment
```
# This will activate your virtualenv.

source env_name/bin/activate
```
* Install django
```
# Running this in your command line will install it to you activated virtual environment

pip install django
```
### 3. Change directory
* Change into the correct folder. You should be in the one containing 'manage.py'.

### 4. Make migrations in Django
```
# Check for any alterations to your project that need migrating

python manage.py makemigrations
```
```
# Make/push any migrations.

python manage.py migrate
```
### 5. Run django server
```
# This will host the web application locally

python manage.py runserver
```

## <a id='video'> Video Demo </a>

For this project, we were required to make a video displaying our web application's functionality. Feel free to watch this short exmaple of the final product. There are timestamps in the bio showing each of the implemented features.

<a href= 'https://youtu.be/dPfLyy0nitk'>
<img width="1494" alt="Thumbnail" 
 src="https://github.com/JosephLambon/Auctions/assets/107887718/07a467af-3e26-4bdf-91e7-e3eb0a3ad814">
</a>




