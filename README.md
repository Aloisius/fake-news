# fake-news

A small project that I use to visually tag links to fake news sites,
fringe sites, pulitzer prize winning sites and opinion urls.

Currently, there is a simple script to convert the various URL
lists I curated into a stylesheet for reddit:

![](docs/screenshot.png?raw=true)


## To Use Reddit Stylesheet

### With [RedditEnhancementSuite](https://redditenhancementsuite.com)

Add the stylesheet by going to settings / appearance / stylesheet loader. Under loadStyleSheets, add a row with the following URL:

https://cdn.rawgit.com/Aloisius/fake-news/master/reddit/tweaks.css

### With [Stylish for Firefox/Chrome/Safari/etc](https://userstyles.org/)

You can install the following user style:

https://userstyles.org/styles/136035/reddit-fake-news-tagger

### With [Stylebot for Chrome](https://chrome.google.com/webstore/detail/stylebot/oiaejidbmkiecgbjeifoejpgmdaleoha)

You can install this style:

http://stylebot.me/styles/15677


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

# Match al.com/birmingham/*
al.com/birmingham/
# or
al.com$ ^/birmingham/

# Match */opinion/* at nytimes.com$
nytimes.com$ /opinion/
```


## To rebuild

```
$ cd reddit
$ ./go.sh
```
