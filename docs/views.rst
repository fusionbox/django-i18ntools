Views
=====

.. currentmodule:: i18ntools.views

.. class:: SetLanguageView

    Available as :func:`set_language`

    If you are using :func:`~django:django.conf.urls.i18n.i18n_patterns` in
    your URL patterns, the :func:`~django:django.views.i18n.set_language` view
    that Django provides won't work for you. The built-in ``set_language``
    view works by :func:`~django:django.utils.translation.activate`-ing the
    language and then returning a redirect back to the exact same URL.
    However, because the URL contains the language information,
    LocaleMiddleware will decide to display the page in the old language, not
    the new language.

    Instead of using the :func:`~django:django.utils.translation.activate`
    function, :class:`SetLanguageView` changes the language by redirecting the
    user to the language-prefixed version of that page.
    :class:`SetLanguageView` uses :func:`i18ntools.utils.url_for_language` to
    transform the URL.

    :class:`SetLanguageView` accepts a ``next`` query string parameter just
    like the built-in view. If the ``next`` parameter is not present or
    invalid, :class:`SetLanguageView` will fall back on to the
    ``HTTP_REFERER``.

    .. attribute :: url

        A fallback URL to redirect to return if neither the ``next`` query
        parameter are present or valid. Defaults to ``/``.

    You can use the :class:`SetLanguageView` by adding it to your URL patterns. ::

        urlpatterns += i18n_patterns('',
            url(r'i18n/$', 'i18ntools.views.set_language', name='set_language'),
          )
