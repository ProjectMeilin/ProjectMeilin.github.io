#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kilfu0701'
SITENAME = u'徴音梅林'
SITE_DESCRIPTION = u'自由なソフトウェア バーチャルシンガーです。使い方はあなたの創意工夫次第です。'
DEFAULT_LANG = 'ja'
SITEURL = 'http://projectmeilin.github.io'
SITEURL_WITH_L10N = '/' + DEFAULT_LANG
SITESUBTITLE = (
    u'<div id="site-desc">'
    u' <div class="side-desc-line">自由なソフトウェア バーチャルシンガーです。使い方はあなたの創意工夫次第です。</div>'
    u' <div class="side-desc-line">語言：<span class="japanese">日本語</span>、<span class="mandarin">台湾式中国語</span></div>'
    u'</div>'
)
PATH = 'content/ja'

TIMEZONE = 'Asia/Taipei'
LOCALE = 'en_US.UTF-8'
GOOGLE_ANALYTICS = True
DATE_FORMATS = {
    'en': '%Y-%m-%d %H:%M',
    'ja': '%Y-%m-%d %H:%M (%a)',
    'zh': '%Y-%m-%d %H:%M',
}

#ARTICLE_URL = 'archives/{slug}/'
#ARTICLE_SAVE_AS = 'archives/{slug}/index.html'
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
FILENAME_METADATA = '(?P<slug>.*)'  # use markdown file name as the slug meta
USE_FOLDER_AS_CATEGORY = True       # use folder name as posts' category
ARTICLE_URL = '{lang}/{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html' #ARTICLE_URL
ARTICLE_LANG_URL = '{lang}/{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = DEFAULT_LANG + '/category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'


# Load plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary', 'read_more_link']
READ_MORE_LINK = u'<div class="read_more">続きを読む..</div>'
#I18N_SUBSITES = {
#    'ja': {
#        'SITENAME': '',
#        }
#    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    #('Python.org', 'http://python.org/'),
    #('Jinja2', 'http://jinja.pocoo.org/'),
    #('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    #('You can add links in your config file', '#'),
    #('Another social link', '#'),
)

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    (u'プロジェクト', 'https://github.com/ProjectMeilin', '_blank'),
    (u'ダウンロード', '/' + DEFAULT_LANG + '/download/index.html', ''),
    (u'使い方', '/' + DEFAULT_LANG + '/document/index.html', ''),
    (u'連絡先', '/' + DEFAULT_LANG + '/help/contact.html', ''),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/pelican-cait-custom'

DISQUS_SITENAME = 'meilin'
USE_OPEN_GRAPH = True
