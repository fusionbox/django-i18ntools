try:
    from urllib.parse import urlparse, urlunparse
except ImportError: # Python 2
    from urlparse import urlparse, urlunparse

from itertools import chain

from django.utils.translation import get_language


def url_for_language(url, new_language):
    """
    Takes a URL and a target language and adds the i18n_patterns prefix for
    that target language.
    """
    current_prefix = '/' + get_language() + '/'
    new_prefix = '/' + new_language
    parts = urlparse(url)
    path = parts.path
    if path.startswith(current_prefix):
        path = path[len(current_prefix) - 1:]
    path = new_prefix + path
    # urlunparse expects a 6-tuple with path as the 3 element.
    return urlunparse(chain(parts[:2], [path], parts[3:]))
