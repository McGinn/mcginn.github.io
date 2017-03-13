# Extend pelicanconf.py and apply some additional settings
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

RELATIVE_URLS = False
OUTPUT_PATH = 'output/'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-23913932-1"
