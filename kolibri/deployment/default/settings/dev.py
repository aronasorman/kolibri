# Enable remote debugging for VSCode
from .base import *  # noqa

import ptvsd
ptvsd.enable_attach("theworstkeptsecret", address=("0.0.0.0", 8010))

DEBUG = True