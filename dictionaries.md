# My XWord Dictionaries

### Simpsons (`simpsons.dict`)

Sourced from [The Simpsons cast](https://en.wikipedia.org/wiki/List_of_The_Simpsons_cast_members), and Simpsons Guest Starts [pt. 1](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_1%E2%80%9320)) and [pt. 2](https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars)

Raw data grabbed with:
```javascript
rows = $('table.sortable th[scope="row"] a')
res = {}
count = 0
$.each(rows, function(i) { if (rows.eq(i).attr('title') && !rows.eq(i).attr('title').includes('does not exist')) {res[rows.eq(i).text()] = true; count++ }})
results = Object.keys(res)
// console.log('num results:', results.length)
// console.log('before dedupe:', count)

for (i = 0; i < results.length; i++) { 
    console.log(results[i]); 
}
```