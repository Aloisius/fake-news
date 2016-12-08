# fake-news

Curated lists of fringe, opinion and pulitzer prize winning news sites as well
as a reddit stylesheet to visually tag links to them appropriately.

If you have your own list which classify sites or sections of sites, please let
me know so I can include it.

## Lists

There are currently 5 separate lists of 270 URLs and sites:

* [fakenews-aloisius](lists/fakenews-aloisius.txt) - Fringe media sites that engage in yellow journalism, conspiracies, rumors, gossip, sensationalism, tabloid journalism, fake news, propaganda, etc.
* [fakenews-snopes](lists/fakenews-snopes.txt) - Fake news sites from snopes.com
* [fakenews-zidmars](lists/fakenews-zidmars.txt) - An edited list of fake news sites from Melissa Zimdars
* [fakenews-fakenewschecker](lists/fakenews-fakenewschecker.txt) - A list of fake news sites from fakenewschecker.com
* [satire-fakenewschecker](lists/satire-fakenewschecker.txt) - A list of satire sites from fakenewschecker.com
* [opinion-fakenewschecker](lists/opinion-fakenewschecker.txt) - A list of opinion sites from fakenewschecker.com
* [opinion-aloisius](lists/opinion-aloisius.txt) - Opinion and commentary news sites as well as opinion sections of mainstream news sites
* [pulitzer-aloisius](lists/pulitzer-aloisius.txt) - Pulitzer prize winners for Journalism since 1981 (excluding commentary & photography)


### List Format

Lists are formatted with either "host/path" or "host path" on each line with support for simple prefix (^), suffix ($),
substring on the hostname or path.

Comments begin with a hash (#).

Examples:

```bash
# Match anything to http://breitbart.com or any subdomain
# (e.g. http://www.breitbart.com)
breitbart.com$

# Match http://bigstory.ap.org/news/ exactly
^bigstory.ap.org/news/$
# or
^bigstory.ap.org$ ^/news/$

# Match any URL with the prefix of http://al.com/birmingham/
# (e.g. http://al.com/birmingham/ and http://al.com/birmingham/article/123
al.com/birmingham/
# or
al.com$ ^/birmingham/

# Match any URL containing /opinion/ in the path at nytimes.com or any subdomain
# (e.g. http://www.nytimes.com/pages/opinion/index.html)
nytimes.com$ /opinion/
```


## To Use Reddit Stylesheet

![](docs/screenshot.png?raw=true)

### With [RedditEnhancementSuite](https://redditenhancementsuite.com)

Add the stylesheet by going to settings / appearance / stylesheet loader. Under loadStyleSheets, add a row with the following URL:

https://cdn.rawgit.com/Aloisius/fake-news/master/reddit/tweaks.css

### With [Stylish for Firefox/Chrome/Safari/etc](https://userstyles.org/)

You can install the following user style:

https://userstyles.org/styles/136035/reddit-fake-news-tagger

### With [Stylebot for Chrome](https://chrome.google.com/webstore/detail/stylebot/oiaejidbmkiecgbjeifoejpgmdaleoha)

You can install this style:

http://stylebot.me/styles/15677


### To rebuild the Reddit Stylesheet

```
$ cd reddit
$ ./go.sh
```

## Usage

<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="http://i.creativecommons.org/p/mark/1.0/88x31.png"
     style="border-style: none;" alt="Public Domain Mark" />
</a>
</p>

This work is free of known copyright restrictions.
