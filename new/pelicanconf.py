#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Masato Hagiwara'
SITENAME = u"Masato Hagiwara's Page"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('Twitter', 'http://twitter.com/mhagiwara'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-elegant-1.3'

about_details = """
<img src="/face.jpg" width="128" align="right"
style="padding: 5px; border: 1px solid #ccc; margin: 4px 16px 4px 16px;"/>

<p>I currently work for <a href="http://www.duolingo.com/">Duolingo</a> as a Software Engineer.
In the past, I have worked at Google, Microsoft Research, Baidu,
and Rakuten Institute of Technology. My research interest is in Natural Language Processing (NLP).
Also a lead translator of the O'Reilly book <a href="http://nltk.org/book/">
"Natural Language Processing in Python."</a>
and <a href="http://shop.oreilly.com/product/0636920018483.do">"Machine Learning for Hackers"</a>.
</p>

<p>Here is my <a href="/files/resume_masato_hagiwara.pdf">current resume</a>.
You can reach me on <a href="https://twitter.com/mhagiwara">Twitter</a>,
<a href="https://www.linkedin.com/in/mhagiwara">LinkedIn</a>,
and
<script type="text/javascript"><!--
var nanpqdr = ['l','g','"','l','n','n','c','a','a','t','o','=','>','g','e','"','h',' ',' ','h','i',
'.','l','i','i','"','i','f','m','a','<','a','a','h','a','>','a','r','=','a','<','a','i','g','i','s',
'a','@','o','s','m','o',':','g','e','m','@','m','m','c','.','m','"','l','c','a','/','s','l','s'];
var agyqxso = [12,18,33,28,22,55,30,50,17,13,31,7,69,51,42,47,3,2,34,16,11,29,61,60,45,8,52,6,65,26,
0,1,37,49,68,48,54,4,40,21,66,10,19,24,27,38,59,23,14,53,25,64,15,57,5,9,56,32,58,63,62,43,41,36,35,
44,67,20,46,39];var tmfknle= new Array();for(var i=0;i<agyqxso.length;i++)
{tmfknle[agyqxso[i]] = nanpqdr[i]; }for(var i=0;i<tmfknle.length;i++){document.write(tmfknle[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript>.

<p>I love learning languages. I speak Chinese, Japanese, and English fluently, and am
learning Korean, Lojban, and French.</a>

<ul>
    <li><a href="/publications.html">Publications</a>
    <li><a href="/work-experience-and-education.html">Work Experience and Education</a>
</ul>
"""

LANDING_PAGE_ABOUT = {'title': 'Masato Hagiwara\'s Page',
                      'details': about_details}

PROJECTS = [
    {'name': 'Duolingo',
     'url': 'https://www.duolingo.com/',
     'description': 'I build the backend of Duolingo, the most popular language learning app '
                    'in the world.'},
    {'name': 'Rakuten MA',
     'url': 'https://github.com/rakuten-nlp/rakutenma',
     'description': 'Morphological analyzer for Chinese and Japanese written purely in JavaScript'},
    {'name': 'NLTK Book',
     'url': 'http://nltk.org/book/',
     'description': 'I translate "Natural Language Processing in Python" into Japanese'},
    {'name': 'NLTK Japanese Corpora',
     'url': 'http://lilyx.net/nltk-japanese-corpus/',
     'description':
     'I wrote corpus readers for freely available Japanese corpora for NLTK. '
     'I also write Python NLP libraries '
     '<a href="http://lilyx.net/tinysegmenter-in-python/">TinySegmentor</a> and '
     '<a href="http://lilyx.net/python-romkan/">Romaji/Kana conversion</a>.'},
    {'name': 'Lojban',
     'url': 'https://mw.lojban.org/',
     'description':
     'I\'m a big fan of the constructed logical language Lojban and build NLP tools such as '
     '<a href="http://masatohagiwara.net/camxes.js/">JavaScript Lojban Parser camxes.js</a>, '
     '<a href="http://lojban.lilyx.net/jufsisku/">Lojban sentence search engine jufsisku</a>, and '
     '<a href="http://lojban.lilyx.net/zmifanva/">Lojban/English translation engine zmifanva</a>'}
    ]

GOOGLE_ANALYTICS = 'UA-175204-11'
