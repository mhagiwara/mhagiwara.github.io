#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Masato Hagiwara'
SITEURL = 'http://localhost:8000'
SITENAME = u'米国で働く機械学習エンジニアのブログ'
SITETITLE = u'米国で働く機械学習エンジニアのブログ'
SITESUBTITLE = u'米国でフリーの機械学習・自然言語処理エンジニア・コンサルタントとして働いています。機械学習・自然言語処理、英語・中国語学習などのトピックが中心です。'
SITEDESCRIPTION = SITESUBTITLE
SITELOGO = 'http://masatohagiwara.net/face.jpg'

THEME = './Flex'
PATH = 'content'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'ja'
DEFAULT_LANG = 'ja'
OG_LOCALE = 'ja_JP'
LOCALE = 'ja_JP.UTF-8'

DATE_FORMATS = {
    'en': '%B %d, %Y',
    'ja': u'%Y-%m-%d(%a)',
}

DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('ブログトップ', 'http://masatohagiwara.net/blog/'),
         ('著者個人ページ', 'http://masatohagiwara.net/'))

# Social widget
SOCIAL = (('github', 'https://github.com/mhagiwara'),
          ('twitter', 'https://twitter.com/mhagiwara_ja'),
          ('rss', 'feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

COPYRIGHT_YEAR = 2019
COPYRIGHT_NAME = 'Masato Hagiwara'

GOOGLE_ANALYTICS = 'UA-175204-11'

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-7401771876348738',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}
