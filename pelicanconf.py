#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kilfu0701'
SITENAME = u'徵音梅林'

# Test for local, leave it blank.
SITEURL = ''  #'https://projectmeilin.github.io'
SITESUBTITLE = (
    u'一個真正自由的虛擬歌手，任你發想各種創意。'
    u'<br>'
    u'語言：<span class="japanese">日語</span>、<span class="mandarin">華語</span>'
    u'<br>'
    u'&#10071; <span class="japanese">日語</span>已完成，<span class="mandarin">華語</span>製作中'
)

PATH = 'content'

TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'zh'
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
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = '{lang}/{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL


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
    ('Project', 'https://github.com/ProjectMeilin', '_blank'),
    ('Download', '//projectmeilin.github.io/zh/download/index.html', ''),
    ('Document', '//projectmeilin.github.io/zh/document/index.html', ''),
    ('Contact', '//projectmeilin.github.io/zh/help/contact.html', ''),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/pelican-cait-custom'

DISQUS_SITENAME = 'meilin'

