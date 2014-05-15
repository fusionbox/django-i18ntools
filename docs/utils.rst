Utility Functions
=================

django-i18ntools provides a utility function for converting the i18n prefix on
a URL.


.. currentmodule:: i18ntools.utils


.. function:: language_context(language_code)

    Returns a context manager with the language specified enabled.  The
    previous language will restored on exit.

        >>> from django.utils.translation import ugettext
        >>> from i18ntools.utils import language_context
        >>> with language_code('es'):
        >>>     ugettext(u'Hello')
        u'Hola'
        >>> ugettext(u'Hello')
        u'Hello'

.. function:: url_for_language(url, language_code)

  
    Takes a URL for the current language and a target language and adds the
    i18n_patterns prefix for that target language.  It does this using two
    strategies, first by resolving the URL and the re-reversing it using the
    new language, if that doesn't work (for example if the URL doesn't exist in
    the URLConf), then :func:`url_for_language` will try to simply substitute
    the language code in the URL. ::

        >>> from django.utils.translation import activate
        >>> from i18ntools.utils import url_for_language
        >>> activate('en')
        >>> url_for_language('/en/about-us/', 'es')
        '/es/about-us/'

    :func:`url_for_language` also works for full URLs.

        >>> url_for_language('http://example.com/en/path/to/page/', 'zh')
        'http://example.com/zh/path/to/page/'
