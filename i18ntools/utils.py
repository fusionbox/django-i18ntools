try:
    from urllib.parse import urlparse, urlunparse
except ImportError: # Python 2
    from urlparse import urlparse, urlunparse

from itertools import chain
from contextlib import contextmanager

from django.utils.translation import get_language, activate
from django.core import urlresolvers
from django.http import Http404


@contextmanager
def language_context(new_language):
    current_language = get_language()
    activate(new_language)
    yield
    activate(current_language)


def _url_for_language_resolve_view(url, new_language):
    """
    Figure out the new URL by resolving the old URL and re-reversing it using
    the new language.
    """
    view = urlresolvers.resolve(url)
    with language_context(new_language):
        new_url = urlresolvers.reverse(view.url_name, args=view.args, kwargs=view.kwargs)
    return new_url


def _url_for_language_brute_force(url, new_language):
    current_prefix = '/' + get_language() + '/'
    new_prefix = '/' + new_language
    parts = urlparse(url)
    path = parts.path
    if path.startswith(current_prefix):
        path = path[len(current_prefix) - 1:]
    path = new_prefix + path
    # urlunparse expects a 6-tuple with path as the 3 element.
    return urlunparse(chain(parts[:2], [path], parts[3:]))


def url_for_language(url, new_language):
    """
    Takes a URL and a target language and adds the i18n_patterns prefix for
    that target language.
    """
    try:
        return _url_for_language_resolve_view(url, new_language)
    except Http404:
        return _url_for_language_brute_force(url, new_language)
