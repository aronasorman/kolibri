# Settings used mainly to ensure that we have all packages we want to bundle,
# added to INSTALLED_APPS during build time.

from .base import * # noqa
from kolibri.utils.pluginfinder import find_external_plugins

def _return_only_uninstalled_apps():
    return set(find_external_plugins()) - set(INSTALLED_APPS)

INSTALLED_APPS = INSTALLED_APPS + list(_return_only_uninstalled_apps())
