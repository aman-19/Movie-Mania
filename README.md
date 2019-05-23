# Movie-Mania
Simple Django Application which autocomplete movie names on given prefix and give information about movie scrapped from IMDb. 


## Files
- **Django App** - Main Django application with 2 APIs:
  1. Retrieve movie data of a given movie id.
  2. Autocomplete a given prefix, retrieving matching movie information.

- **Scrapper** - Here you will find scrapper used to scrap data off the IMDb site.

- **Trie** - Main idea behind the autocomplete feature is to use basic **trie data structure**. Implementation of trie data structure along with auto complete using constructed trie can be found here.


## How to use

Well you can check yourself if this works or not. Hopefully you have cloned or downloaded before using ;D
Before you proceed make sure you have Django installed. 
1. Start a [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) and navigate to repo directory where **manage.py** is located.

2. Run command - **python manage.py makemigrations**

3. Run command - **python manage.py migrate**

Above two commands are used only when running App for the first time, just to check and apply settings. They are not needed when running local server again.

4. Run command - **python manage.py runserver**
  This will run a Django server on your local system which can be accessed in browser at [localhost](http://127.0.0.1:8000/)

**Note :- Database used is sqlite beacuse of its easy portability. You will not have to create database. But it is recommended to use PostgreSQL or MongoDB.**
