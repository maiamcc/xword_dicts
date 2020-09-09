# My XWord Dictionaries

### Celebs ([`celebs.dict`](/celebs.dict))

Sourced from:
* [The Simpsons cast](https://en.wikipedia.org/wiki/List_of_The_Simpsons_cast_members), and Simpsons Guest Stars [pt. 1](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_1%E2%80%9320) and [pt. 2](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars), because it's a Who's Who of actors and other celebrities
* [IMDB 100 Most Popular Celebrities](https://www.imdb.com/list/ls052283250/)
* [Wikipedia's Most Viewed Pages: People](https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#People)

Raw data grabbed from Simpsons guest star pages with:
```javascript
rows = $('table.sortable th[scope="row"] a')
res = {}
$.each(rows, function(i) {
  if (rows.eq(i).attr('title') &&
      !rows.eq(i).attr('title').includes('does not exist')) {
    res[rows.eq(i).text()] = true;
  }
})
results = Object.keys(res)

for (i = 0; i < results.length; i++) { 
    console.log(results[i]); 
}
```
Otherwise, just copy/paste.

### Future work
* scrape Urban Dictionary
* scrape any number of wiki categories and then rank popularity
* The Simpsons locations
* top N lists
* NYT_first_said bot
* some slang dictionary
* Simpsons characters and places (see [characters](https://en.wikipedia.org/wiki/List_of_The_Simpsons_characters) and [recurring characters](https://en.wikipedia.org/wiki/List_of_recurring_The_Simpsons_characters#TOP), [Springfield](https://en.wikipedia.org/wiki/Springfield_(The_Simpsons))

#### See also:
* https://github.com/stephthegeek/Crossword-Dictionaries
