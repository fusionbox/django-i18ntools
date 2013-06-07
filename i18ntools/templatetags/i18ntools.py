from __future__ import absolute_import

from django.template import Library
from django.core.urlresolvers import reverse

from i18ntools.utils import url_for_language


register = Library()


@register.simple_tag
def i18nurl(language_code, view, *args, **kwargs):
    url = reverse(view, args=args, kwargs=kwargs)
    return url_for_language(url, language_code)


register.filter('url_for_language', url_for_language)
