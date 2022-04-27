#!/usr/bin/env python3

AUTHOR = 'kilfu0701'
SITENAME = '徵音梅林'
SITE_DESCRIPTION = '一個真正自由的虛擬歌手，任你發想各種創意。'
DEFAULT_LANG = 'zh'
SITEURL = '//projectmeilin.github.io'
SITEURL_WITH_L10N = '/' + DEFAULT_LANG
SITESUBTITLE = (
    '<div id="site-desc">'
    ' <div class="side-desc-line">一個真正自由的虛擬歌手，任你發想各種創意。</div>'
    ' <div class="side-desc-line">語言：<span class="japanese">日語</span>、<span class="mandarin">華語</span></div>'
    #' &#10071; <span class="japanese">日本語ONLY</span>版，<span class="mandarin">日華語</span>版'
    '</div>'
)
PATH = 'content/zh'

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
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = '{lang}/{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = DEFAULT_LANG + '/category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'


# Load plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary', 'read_more']
SUMMARY_MAX_LENGTH = 100
SUMMARY_END_SUFFIX = '...'
READ_MORE_LINK = '<div class="read_more">更多內容..</div>'
#READ_MORE_LINK_FORMAT = '<a class="read-more" href="/{url}">{text}</a>'
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
    ('關於專案', 'https://github.com/ProjectMeilin', '_blank'),
    ('下載檔案', '/' + DEFAULT_LANG + '/download/index.html', ''),
    ('教學文件', '/' + DEFAULT_LANG + '/document/index.html', ''),
    ('聯絡我們', '/' + DEFAULT_LANG + '/help/contact.html', ''),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/pelican-cait-custom'

DISQUS_SITENAME = 'meilin'
USE_OPEN_GRAPH = True
