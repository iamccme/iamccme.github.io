#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CC'
SITENAME = u'world of CC'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
THEME = 'tuxlite_tbs'
DISQUS_SITENAME = 'iamccme'
GOOGLE_ANALYTICS = 'UA-43278130-1'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Blogroll
LINKS =  (('Google', 'https://www.google.com/ncr'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
          ('lizherui的程序世界', 'http://www.lizherui.com/')
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/lizherui'),
          ('Twitter', 'https://twitter.com/iamccme'),
          ('Weibo', 'http://weibo.com/iamccme'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
