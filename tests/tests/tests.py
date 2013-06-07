"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import urllib

from django.test import TestCase
from django.utils.translation import activate
from django.template import Template, Context
from django.core.urlresolvers import reverse


from i18ntools.utils import url_for_language


def build_url(path, **kwargs):
    if kwargs:
        path += '?' + urllib.urlencode(kwargs)
    return path


class UrlForLanguageTest(TestCase):
    def test_no_language(self):
        activate('en')
        self.assertEqual(url_for_language('/about/', 'en'), '/en/about/')
        self.assertEqual(url_for_language('/about/', 'es'), '/es/about/')

    def test_with_language(self):
        activate('en')
        self.assertEqual(url_for_language('/en/about/', 'en'), '/en/about/')
        self.assertEqual(url_for_language('/en/about/', 'es'), '/es/about/')

    def test_with_host(self):
        activate('en')
        url = 'http://example.com/en/about/'
        self.assertEqual(url_for_language(url, 'es'), 'http://example.com/es/about/')

    def test_with_weirder_prefix(self):
        activate('en-us')
        self.assertEqual(url_for_language('/en-us/about/', 'es'), '/es/about/')

        activate('es')
        self.assertEqual(url_for_language('/es/about/', 'es-mx'), '/es-mx/about/')

    def test_possible_false_positive(self):
        activate('en')
        self.assertEqual(url_for_language('/enable/', 'en'), '/en/enable/')
        self.assertEqual(url_for_language('/enable/', 'es'), '/es/enable/')


class TemplateTagsTest(TestCase):
    urls = 'tests.urls'

    def render(self, template, **context):
        t = Template("{% load i18ntools %}" + template)
        return t.render(Context(context)).strip()

    def test_i18nurl_no_args(self):
        activate('en')
        self.assertEqual(self.render("{% i18nurl 'en' 'test' %}"), '/en/')
        self.assertEqual(self.render("{% i18nurl 'es' 'test' %}"), '/es/')

    def test_i18nurl_with_args(self):
        activate('en')
        self.assertEqual(self.render("{% i18nurl 'en' 'args' 1 2 %}"), '/en/1/2/')
        self.assertEqual(self.render("{% i18nurl 'es' 'args' 2 3 %}"), '/es/2/3/')

    def test_i18nurl_with_kwargs(self):
        activate('en')
        self.assertEqual(self.render("{% i18nurl 'en' 'kwargs' k1=1 k2=2 %}"), '/en/1/2/')
        self.assertEqual(self.render("{% i18nurl 'es' 'kwargs' k1=2 k2=3 %}"), '/es/2/3/')

    def test_url_for_language(self):
        activate('en')
        self.assertEqual(self.render("{{ test|url_for_language:'en' }}", test='/en/about/'), '/en/about/')
        self.assertEqual(self.render("{{ test|url_for_language:'es' }}", test='/en/about/'), '/es/about/')


class SetLanguageViewTest(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        activate('en')
        self.url = reverse('set_language')

    def assertRedirects(self, response, expected_url, status_code=301,
                        target_status_code=404, **kwargs):
        return super(SetLanguageViewTest, self).assertRedirects(
            response, expected_url, status_code, target_status_code, **kwargs
        )

    def test_no_referer(self):
        resp = self.client.post(self.url, {'language': 'es'})
        self.assertRedirects(resp, '/es/', 301)

        resp = self.client.post(self.url, {'language': 'es'})
        self.assertRedirects(resp, '/es/', 301)

    def test_with_good_referer(self):
        resp = self.client.post(self.url, {'language': 'es'},
                                HTTP_REFERER='/en/refered/')
        self.assertRedirects(resp, '/es/refered/', 301)

    def test_with_bad_referer(self):
        resp = self.client.post(self.url, {'language': 'es'},
                                HTTP_REFERER='http://badexample.com/')
        self.assertRedirects(resp, '/es/', 301)

    def test_with_good_next_url(self):
        good_url = build_url(self.url, next='/en/nexted/')
        resp = self.client.post(good_url, {'language': 'es'})
        self.assertRedirects(resp, '/es/nexted/', 301)

    def test_with_bad_next_url(self):
        bad_url = build_url(self.url, next='http://badexample.com/')
        resp = self.client.post(bad_url, {'language': 'es'})
        self.assertRedirects(resp, '/es/', 301)

    def test_with_bad_next_url_but_good_referer(self):
        bad_url = build_url(self.url, next='http://badexample.com/')
        resp = self.client.post(bad_url, {'language': 'es'},
                                HTTP_REFERER='/en/refered/')
        self.assertRedirects(resp, '/es/refered/', 301)
