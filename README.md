# Movie-Mania
Simple Django Application which autocomplete movie names on given prefix and give information about movie scrapped from IMDb. 

## Files
- **Django App** - Main Django application with 2 APIs:
  1. Retrieve movie data of a given movie id.
  2. Autocomplete a given prefix, retrieving matching movie information.

- **Scrapper** - Here you will find scrapper used to scrap data off the IMDb site.

- **Trie** - Main idea behind the autocomplete feature is to use basic **trie data structure**. Implementation of trie data structure along with auto complete using constructed trie can be found here.
