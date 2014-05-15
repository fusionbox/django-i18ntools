from __future__ import absolute_import

from django.template import Library
from django.core.urlresolvers import reverse

from i18ntools.utils import url_for_language, language_context


register = Library()


@register.simple_tag
def i18nurl(language_code, view, *args, **kwargs):
    with language_context(language_code):
        return reverse(view, args=args, kwargs=kwargs)


register.filter('url_for_language', url_for_language)
