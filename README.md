# XWord Dictionaries

I've written some slap-dash utils for my own use in creating and cleaning crossword dictionaries (primarily for use with [Crossfire](http://beekeeperlabs.com/crossfire/))

## Utils
This repo contains a handful of utils that can be invoked via:
```
./script.py <command> <args>
```

Most commands take a `filename` arg; this should be the path to a file containing a newline-separated list of raw entries to be manipulated. (Copy+paste these off the Internet, fetch via an API, scrape a website, whatever.)
 
### Available commands are:

#### `dedupe [filename]`
Dedupe the list at $FILENAME, output to a new file.

#### `combinate [filename]`
Most useful on lists of names. For the list at $FILENAME, generate crossword candidates for each entry: specifically, every individual (space-separated) element of the entry (if not already an accepted Crossfire word), and every pairwise combination of sequential elements. Output to a new file.

E.g. the name `John Philip Sousa` would generate candidates: `John Philip Sousa`, `John`, `Philip`, `Sousa`, `John Philip`, `Philip Sousa`.

#### `rank [filename]`
For the list at $FILENAME, query the [Wikimedia Pageview API](https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews) to get the views-per-month of each entry's Wikipedia page (since Jan. 2019), and output a sorted list to a new file. I use this as a proxy for how well-known an entry is.

Recommend usage: remove (or manually vet) all entries with < n views-per-month (where n is an arbitrary number, I use 10,000).

#### `vet [filename]`
For the list at $FILENAME, present each entry and let user indicate with `y/n` whether to keep that entry. Output the approved entries to a new list. (If you need to stop the vet partway through, your progress will be saved in an interim file.)

Useful for combing through a list of spotty data and deciding what to keep.

### Recommended flow:
1. get raw data from source (API, scrape, copy+paste from a "top 100" list, etc.), save as newline-separated list at `data.raw`
2. dedupe
3. rank entries, cut (or manually vet) the least viewed and no-page-found entries
4. (optional) combinate entries to get even more crossword candidates
5. vet results (manually or via the util) and save as dict

## Dictionaries
 
### Celebs ([`celebs.dict`](/dictionaries/celebs.dict))

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
