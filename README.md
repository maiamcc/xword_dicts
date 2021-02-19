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

#### `transform [fromstr] [tostr]`
For all elements from all dictionaries (the crossfire default dictionary and the `.dict` files in the `dictionaries/` directory of this repo), find those that are still valid dictionary elements when all instances of `fromstr` are replaced with `tostr`.

### Recommended flow:
1. get raw data from source (API, scrape, copy+paste from a "top 100" list, etc.), save as newline-separated list at `data.raw`
2. dedupe
3. rank entries, cut (or manually vet) the least viewed and no-page-found entries
4. (optional) combinate entries to get even more crossword candidates
5. vet results (manually or via the util) and save as dict

## Dictionaries

#### A note on scoring

I've scored these dictionaries roughly using [the rules proposed here](https://www.alexboisvert.com/xwordlist/guidelines.php). Scores are a verrrry rough estimate based mostly on how well _I_ know the terms in these lists/how excited _I personally_ would be to see them in a crossword, and so are inherently going to be shaped by my own exposures, biases, etc. Take these with many grains of salt and please re-score where appropriate!

### Words ([`nltk-words-full.dict`](/dictionaries/nltk-words-full.dict))
A big ol' wordlist from [NLTK's `words` corpus](https://www.nltk.org/book/ch02.html#homonyms_index_term). Not scored and never will be--just an attempt to fill in the gaps of Crossfire's default wordlist.

### Celebs ([`celebs-scored.dict`](/dictionaries/celebs-scored.dict))

Sourced from:
* [The Simpsons cast](https://en.wikipedia.org/wiki/List_of_The_Simpsons_cast_members), and Simpsons Guest Stars [pt. 1](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_1%E2%80%9320) and [pt. 2](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars), because it's a Who's Who of actors and other celebrities
* [IMDB 100 Most Popular Celebrities](https://www.imdb.com/list/ls052283250/)
* [Wikipedia's Most Viewed Pages: People](https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#People)
* Manual [UrbanDictionary](https://www.urbandictionary.com/) combing

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

### Websites & Apps ([`websites-scored.dict`](/dictionaries/websites-scored.dict))

Popular websites and apps. (Because of the nature of the source material, contains lots of news media, too.)

Sourced from:
* [Moz.com's "Top 500 Websites"](https://moz.com/top500)
* [Wikipedia: Most Popular Smartphone Apps](https://en.wikipedia.org/wiki/List_of_most_popular_smartphone_apps)
* [Wikipedia: Most Downloaded iOS Apps](https://en.wikipedia.org/wiki/App_Store_(iOS)#Most_downloaded_apps)
* [Wikipedia: Most Downloaded Android Apps](https://en.wikipedia.org/wiki/List_of_most-downloaded_Google_Play_applications)

### UrbanDictionary Miscellany ([`urbandictionary-scored.dict`](/dictionaries/urbandictionary-scored.dict))

Honestly I just looked at the top [UrbanDictionary](https://www.urbandictionary.com/) words by letter and the current most popular words and grabbed whatever looked interesting and wasn't already in CrossFire's dictionary (plus some word associating).

This dictionary has since been supplemented with the [Dictionary.com Slang Dictionary](https://www.dictionary.com/e/slang/).

This is not a complete or coherent list of anything; it's just some random slang and also other stuff. (I did my best to remove all inappropriate words but some may have snuck by me.)
### Netspeak ([`netspeak-scored.dict`](/dictionaries/netspeak-scored.dict))
Chat acronyms/abbreviations and netspeak (with some other internet-related words thrown in). Mostly low-scored acronyms suitable for filler, but there are some interesting entries in here too.

Sourced from:
* [Wiktionary: English Internet Slang](https://en.wiktionary.org/wiki/Appendix:English_internet_slang)
* [Lifewire: Internet Slang Dictionary](https://www.lifewire.com/urban-internet-slang-dictionary-3486341)
* [Netlingo: Online Dating Terms](https://www.netlingo.com/shop/Top_50_Online_Dating_Terms.pdf)
* [Netlingo: Acroynms](https://www.netlingo.com/acronyms.php)

### Colleges and Universities ([`colleges-scored.dict`](/dictionaries/colleges-scored.dict))
Sourced from:
* [US News Top Liberal Arts Colleges](https://www.usnews.com/best-colleges/rankings/national-liberal-arts-colleges)
* [The Ivy League](https://en.wikipedia.org/wiki/Ivy_League)

### Queer/LGBTQIA+ ([`queer-scored.dict`](/dictionaries/queer-scored.dict))
Because dear god we need more queer representation in crosswords. Note that just because a word appears in this list does not mean that it's widely used or even necessarily acceptable: e.g. I included "hermaphrodite", which is generally not used for people anymore (instead, use "intersex"), "transsexual", which has fallen out of favor with younger folks (instead, use "transgender"), and "throuple", which no actual polyamorous person I've met would touch with a ten-foot pole (my social circles prefer "triad" or "vee").

Sourced from:
* [San Mateo: LGBTQ Glossary](https://lgbtq.smcgov.org/lgbtq-glossary)
* [The Safe Zone Project: Glossary](https://thesafezoneproject.com/resources/vocabulary/)
* [National LGBT Health Education Center (Fenway Institute): Glossary of LGBT Terms](https://www.lgbtqiahealtheducation.org/wp-content/uploads/LGBT-Glossary_March2016.pdf)

Bonus: the folks at [Queer Qrosswords](https://queerqrosswords.com/) are doing _excellent_ things for queer/LGBTQIA+ representation in the crossword world, go check out their collections!

## Future Work/TODO
* scrape any number of wiki categories and then rank popularity
* The Simpsons locations
* top N lists
* NYT_first_said bot
* Simpsons characters and places (see [characters](https://en.wikipedia.org/wiki/List_of_The_Simpsons_characters) and [recurring characters](https://en.wikipedia.org/wiki/List_of_recurring_The_Simpsons_characters#TOP), [Springfield](https://en.wikipedia.org/wiki/Springfield_(The_Simpsons))
* Comic book characters/superheros
* Games (video games, board games)

#### See also:
* https://github.com/stephthegeek/Crossword-Dictionaries
