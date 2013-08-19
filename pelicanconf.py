#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CC'
SITENAME = u'world of CC'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

DEFAULT_LANG = u'en'

DISQUS_SITENAME = 'iamccme'

GOOGLE_ANALYTICS = 'UA-43278130-1'
# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

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
          ('lizherui的程序世界', 'http://www.lizherui.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/iamccme'),
          ('Twitter', 'https://twitter.com/iamccme'),
          ('Weibo', 'http://weibo.com/iamccme'))

DEFAULT_PAGINATION = 10

