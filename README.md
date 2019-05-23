# Movie-Mania
Simple Django Application which autocomplete movie names on given prefix and give information about movie scrapped from IMDb. 
Simple Trie data structure is used here to match prefix with movie titles.

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

**Note: Database used is sqlite beacuse of its easy portability. You will not have to create database. But it is recommended to use PostgreSQL or MongoDB.**

Now to use and see API in affect specific urls are to be used.

### For retrieving

- **Retrieve whole database or list of movies -** **"http://127.0.0.1:8000/api/movies/"**

- **Retrieve specific movie record -**  Now to retrieve specific record just append or add **<movie_id>** after the link specified above. For example: - **"http://127.0.0.1:8000/api/movies/108/"**

### For Auto-complete

A **prefix** is needed for autocomplete feature to work. Some *parameters* can be used to refine results, the first one obviously being the prefix while the others are : **limit** and **offset**.

 - **Url to use autocomplete -** **"http://127.0.0.1:8000/api/autocomplete?prefix=the"**
  <p> Here, you can see a *parameter "prefix" is paased after '?'* whose value is set to *'the'*. This url will provide movies matching prefix 'the', **sorted according to their ratings in descending order.** </p>

- **Pass 'limit' parameter -** The parameter *limit* here defines the **maximum number of movies in result matching the prefix given.** To pass multiple paramters **'&'** symbol is used. Example :- **"http://127.0.0.1:8000/api/autocomplete?prefix=the&limit=10"** \s\s
This url will now provide **only 10 movies at max matching 'the' prefix with their titles.**

- **Pass 'offset' parameter -** The parameter *offset* here defines that the **the number of movies which will be discarded  in result or skipping first 'offset' number of movies in result obtained after matching titles woth given prefix.** Example :- **"http://127.0.0.1:8000/api/autocomplete?prefix=the&limit=10"** \s\s
Now you will notice, first three movies which were shown in previous url are gone and 3 new movies are there at the end of the result.

**Note: It is optional to provide parameters but *default values of 'limit' and 'offset' are set to '5' and '0' respectively in case parameters are not provided.***
