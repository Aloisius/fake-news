# fake-news

A small project that I use to visually tag links to fake news sites, 
fringe sites, pulitzer prize winning sites and opinion urls.

Currently, there is a simple script to convert the various URL 
lists I curated into a stylesheet for reddit:

![](docs/screenshot.png?raw=true)


## To Use

If using RedditEnhancementSuite, add by going to settings / appearance /
stylesheet loader. Under loadStyleSheets, add a row with the following URL:

https://cdn.rawgit.com/Aloisius/fake-news/master/reddit/tweaks.css


## Lists

A list has allows limited pattern matching to do prefix, suffix, 
substring and exact matches on either the domain or the path.

```
# Match anything at breitbart.com$
breitbart.com$

# Match ^bigstory.ap.org/news/$
^bigstory.ap.org/news/$
# or
^bigstory.ap.org$ ^/news/$

# Match al.com/burmingham/*
al.com/burmingham/
# or
al.com$ ^/burmingham/

# Match */opinion/* at nytimes.com$
nytimes.com$ /opinion/
```


## To rebuild

```
$ cd reddit
$ ./go.sh
```
