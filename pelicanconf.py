# Theme-specific settings
SITENAME = 'Alexander McGinn'
DOMAIN = 'blog.alexandermcginn.com'
BIO_TEXT = 'This is a bio'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>, <a href="http://github.com/iKevinY/pneumatic">Pneumatic</a>, and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'

SITE_AUTHOR = 'Alexander'
INDEX_DESCRIPTION = 'Website and blog of Alexander McGinn.'

SIDEBAR_LINKS = [
        '<a href="/about/">About</a>',
        '<a href="/archive/">Archive</a>',
        ]

ICONS_PATH = 'images/icons'

GOOGLE_FONTS = [
        "Nunito Sans:300,700",
        "Source Code Pro",
        ]

SOCIAL_ICONS = [
        ('mailto:alexander.mcginn@gmail.com', 'Email (alexander.mcginn@gmail.com)', 'fa-envelope'),
        ('/atom.xml', 'Atom Feed', 'fa-rss'),
        ]

THEME_COLOR = '#FF8000'

# Pelican settings
RELATIVE_URLS = True
SITEURL = 'http://blog.alexandermcginn.com'
TIMEZONE = 'Canada/Eastern'
DAFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

THEME = 'pneumatic'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tage, and category tags
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True
MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.codehilite': {'linenums':'True'},
            'markdown.extensions.extra': {},
            'markdown.extensions.admonition': {},
            },
        'output_format': 'html5',
        }

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 'uploads', 'extra']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

extras = ['favicon.ico', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

DEFAULT_LANG = 'en'


PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
        ('cache', False),
        ('manifest', False),
        ('url_expire', False),
        ('versions', False),
        ]
