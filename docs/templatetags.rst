Template Tags
=============

django-i18ntools provides some useful template tags and filters when dealing
with internationalized URLs in templates.

.. currentmodule:: i18ntools.templatetags

Tags
----

.. function:: i18nurl(language_code, view, *args **kwargs)

    Allows you to reverse a URL in a specific language.  For example, if you
    wanted to link to the website in a different language, you could do this.

    .. code-block:: html+django

        <a href="{% i18nurl 'en' 'home' %}">Welcome</a>
        <a href="{% i18nurl 'es' 'home' %}">Bienvenido</a>
        <a href="{% i18nurl 'zh' 'home' %}">欢迎</a>


Filters
-------

.. function:: url_for_language(url, language_code)

    This is a template interface to the
    :func:`i18ntools.utils.url_for_language` function.

    You could use this to show links to the current page in a different
    language for example.

    .. code-block:: html+django

        <a href="{{ request.path|url_for_language:'en' }}">español</a>
