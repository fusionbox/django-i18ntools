Utility Functions
=================

django-i18ntools provides a utility function for converting the i18n prefix on
a URL.


.. currentmodule:: i18ntools.utils

.. function:: url_for_language(url, language_code)

  
    Takes a URL for the current language and a target language and adds the
    i18n_patterns prefix for that target language. ::

        >>> from django.utils.translation import activate
        >>> from i18ntools.utils import url_for_language
        >>> activate('en')
        >>> url_for_language('/en/about-us/', 'es')
        '/es/about-us/'

    :func:`url_for_language` also works for full URLs.

        >>> url_for_language('http://example.com/en/path/to/page/', 'zh')
        'http://example.com/zh/path/to/page/'
