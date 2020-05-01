## How to Use:
To retrieve video links for search term *happiness and joy*:
```
python phuber.py "happiness and joy" 
```
## Positional:
**search terms(REQUIRED)**

This is the term(s) you are searching for.  It is required and needs to be wrapped in quotes if spaces are involved.

## Options:

### Main Settings
<hr>

**-p / --pages *number***

Number of pages to scrape. Default: *1*

**-l / --list_name *"filename.extension"***

Name of output file.  Default: *list.txt*

**-x / --premium *"username:password"***

The login credentials to use when scraping premium pages.  <username:password> format
```
 python phuber.py --premium "username:password" "search term"
```

### Filters
<hr>

**--premium-only**

Retrieve only premium videos. *(must have premium account)*

**-i / --include *"category"***

The category to filter into the search. **See list of categories below*

**-e / --exclude *"[category, ...]"***

The category(ies) to remove from the search **(max=10)**. **See list of categories below*
``` 
python phuber.py -e "cat1,cat2,cat3,cat4" "search term"
``` 

**--prod *"type"***

Production of the video. Choices: *[home, pro]*

**--min / --min-dur *duration***

Minimum length of videos. Choices: *[10,20,30]*

**--max / --max-dur *duration***

Maximum length of videos. Choices: *[10,20,30]*

### Console Prints
<hr>

**--category-list**

List of all available categories to filter through *"(what keyword mean)"*

```
python phuber.py --category-list ""
```
**-v / --verbose**

Prints out the video titles of what your scrapping to console output

## Category Keywords List
**The keywords are the characters **NOT** in parenthesis.* 

Column #1 | Column #2 | Column #3 | Column #4 | Column #5 |
---------- | ----------- | -------- | -------- | ----------|
60fps | amateur | anal | arab | asian | 
bbw *(big busty women)*| babe| babysitter| btscenes *(behind the scenes)*| bigass|
bigdick | titslg *(big tits)*|bimale|blonde|bj *(blowjob)*|
bondage | brazilian | british | brunette|bukkake|
cartoon|casting|celeb|cc|college|
comp *(compilation)*|cosplay|creampie|cuckold|cumshot|
czech|described|dp|ebony|euro|
exclusive|feet|femaleorgy *(female orgasm)*|fetish|fisting|
french|funny|gangbang|gay|german|
hd|handjob|hardcore|hentai|indian|
interactive|interracial|italian|japanese|korean|
latina|lesbian|milf|massage|masturbate|
mature|musclemen|music|oldyoung|orgy|
pov|parody|party|piss|popww *(popular with women)*|
pornstar|public|pussylick|reality|redhead|
rp *(roleplay)*|romantic|rough|russian|sfw|
school|titssm *(small tits)*| smoking|solofemale|solomale|
squirt|step *(step fantasy)*| strip *(striptease)*|tatwomen *(tatooed women)*|teen|
3some|toys|tmale *(transmale)*| twgirl *(trans with girl)*|twguy *(trans with guy)*|
trans *(transgender)*|veramateurs *(verified amateurs)*|vercouples *(verified couples)*| vermodels *(verified models)*| vintage|
vr *(virtual reality)*| webcam


## Epilogue
All scraped urls are dumped into the *list_name* file which can then be used with youtube-dl

Example:

    youtube-dl -a list.txt
    
This command will download best quality videos from the *list_name* file
