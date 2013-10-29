#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = u'chrooted.net'
AUTHOR = u'Patrick Pelletier'
SITESUBTITLE = 'Patrick Pelletier\'s personal webpage...'
SITEURL = 'http://chrooted.net'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

PROFILE_IMAGE_URL = 'https://secure.gravatar.com/avatar/566e0ab0119d534d05abbcf61d316d28?s=300'

TYPOGRIFY = True

THEME = 'themes/crowsfoot'

MENUITEMS = [('blog', '/')]

STATIC_PATHS =['misc', 'img']

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = None

FILES_TO_COPY = (('extra/CNAME', 'CNAME'),)

# addresses

#EMAIL_ADDRESS = 'pp.pelletier@gmail.com'
GITHUB_ADDRESS = 'https://github.com/skinp'
#SO_ADDRESS = 'https://stackoverflow.com/users/2907/skinp'
TWITTER_ADDRESS = 'https://twitter.com/skinp'

# feed
FEED_RSS = 'feeds/rss.xml'
FEED_MAX_ITEMS = 10

SHOW_ARTICLE_AUTHOR = False

LICENSE_NAME = "CC BY-SA"
LICENSE_URL = "https://creativecommons.org/licenses/by-sa/3.0/"
