# Phuber

**Phuber** allows you to retrieve video links primarily from Pornhub.

For ease of use, try the command-line configurator for this tool [here](https://zimtools.vercel.app/phuber)

# Table of Contents

- [Features](#features)
    - [Searching](#searching)
        - [Demonstration](#demonstration)
- [Positional](#positional)
- [Optionals](#options)
    - [Main](#main)
    - [Filters](#filters)
    - [Premium](#premium)
    - [Console Prints](#console-prints)
- [Epilogue](#epilogue)

## Features

### Searching

Phuber has 2 ways to search, *Keyword* & *Category*.

#### Keyword Search

*Keyword search* is the default and allows you to search videos using keywords.

#### Category Search

*Category search* allows you to search video link using a valid category name. With this search
type, you can search video links which fits the criteria of two categories. To add another
category, see `--include,-i`. Also to enable *Category search*, see `--cat-search`.

#### Gay Support

Phuber now supports searching links in the gay category. To do this, start your search term and/or
category choices with `!`.

#### Demonstration

Retrieves video links for search terms *happiness and joy* in the gay category, which
excludes the *group* and *bear* categories while also including the *feet* category:

```commandline
phuber pornhub --exclude="!group,!bear" --include="!feet" "!happiness and joy" 
```

Retrieves video links that are both in the *solo-female* & *funny* categories:

```commandline
phuber pornhub --cat-search --include="funny" "solo-female" 
```

---

## Positional:

**search terms**

Search using keywords or by a category if `--cat-search` is enabled.

## Options:

---

### Main
**--cat-search**

Activate category search. Search by a category instead of by keywords. *See category list for 
options.*

**-p / --pages *number***

Number of pages to scrape. Default: *1*

**-l / --list-name *"filename.extension"***

Name of output file. Default: *list.txt*



---

### Filters

**-i / --include *"category"***

The category to filter into the search. *_See `--category-list`_

**-e / --exclude *"[category, ...]"***

The category(ies) to remove from the search **(max=10)**. *_See `--category-list`_

``` 
phuber pornhub -e "cat1,cat2,cat3,cat4" "search term"
```

**--prod *"type"***

Production of the video. Choices: *[home, pro]*

**--min / --min-dur *duration***

Minimum length of videos. Choices: *[10,20,30]*

**--max / --max-dur *duration***

Maximum length of videos. Choices: *[10,20,30]*

**--order**

Changes ordering of videos in search results. Choices: *[viewed, top, longest, hottest, newest]*. Default: *(by featured/relevancy/top sold)*

**--order-time**

Changes ordering of videos in search results by time. *Only applicable for `top` & `viewed` options*
. Choices *[yearly, monthly, weekly, daily, all]*. Default: *(auto)*

**--promo**

Changes filter videos based on promotion. *Only applicable during category search only.* Choices 
*[premium, paid]*. Default: *(all)*

**--hd**

Show only HD videos.

**--loc *location***

Changes ordering of videos based on location around the world. *Only applicable during 
category search with `hottest` or `viewed` used. *See `--location-list`. * Default: *(auto)* 

---

### Premium

**-x / --premium *"username:password"***

The login credentials to use when scraping premium pages.  <username:password> format

```commandline
phuber pornhub --premium "username:password" "search term"
```

**--premium-only**

Retrieve only premium videos. *(must have premium account)*

--- 

### Console Prints
**-v / --verbose**

Prints out the video titles of what you're scraping to console output

**--category-list**

List of all available categories.

```
phuber pornhub --category-list
```

**--location-list**

List of all available locations.

---

## Epilogue

All scraped urls are dumped into the *list_name* file which can then be used with youtube-dl or any
other video downloader.

Example:

    youtube-dl -a list.txt

This command will download videos from the *list_name* file.
