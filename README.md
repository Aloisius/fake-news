# reddit-style

![](docs/screenshot.png?raw=true)

This was created in order to better judge whether an article should be
trusted based on the reputation of the news source.

This adds a label to links on Reddit if the site is:

* A Pulitzer prize winner for Journalism since 1981 (excluding commentary & photography)
* Fringe media: kooks, cranks, conspiracies, rumors, gossip, sensationalism, tabloid journalism, fake news, propaganda, etc.
* Ideologically driven organizations

It also labels opinion articles to distinguish them from actual reporting.


## To Use


If using RedditEnhancementSuite, add by going to settings / appearance /
stylesheet loader. Under loadStyleSheets, add a row with the following URL:

https://cdn.rawgit.com/Aloisius/reddit-style/master/tweaks.css


## Data

The categories used are arbitrary. Ideally, there would be some sort of letter grade for sources that
encapsulates ethical standards, journalistic integrity, sensationalism and what not.


## To rebuild

```shell
sass tweaks.scss tweaks.css
```

## Lists

For the url http://a.b.c/1/2.html?param=1, the client will try these
possible strings:

a.b.c/1/2.html?param=1
a.b.c/1/2.html
a.b.c/
a.b.c/1/
b.c/1/2.html?param=1
b.c/1/2.html
b.c/
b.c/1/
/1/2.html?param=1
/1/2.html
/1/
/


Entry format:

domain-expression path-expression

domain-expression is domain + ^$ special characters
path-expression is a path to match + ^$ special characters

Short cut format:

domain-suffix-expression/path-prefix-expression

domain-suffix-expression is domain$ + ^ special characters
path-prefix-expression is a ^path to match + $ special characters

Domain-only short cut format:

domain-expression


Read line
if has a space, then it is a standard entry format
if it has a slash, it is a short-cut format
else if it appears to be a domain, it is domain-short-cut format

# Long form:
# domain /path/
# ^domain$ ^/path/$
#
# Short-hand form:
# theguardian.com/commentisfree/ -> theguardian.com$ ^/commentisfree/
#
