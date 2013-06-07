from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns


def dummy_view(*args, **kwargs):
    pass


urlpatterns = i18n_patterns('',
                            url(r'^set-language/', 'i18ntools.views.set_language', name='set_language'),

                            # template tags
                            url(r'^$', dummy_view, name='test'),
                            url(r'^(.*)/(.*)/', dummy_view, name='args'),
                            url(r'^(?P<k1>.*)/(?P<k2>.*)/', dummy_view, name='kwargs'),
                            url(r'^(.*)/(?P<k1>.*)/', dummy_view, name='mixed'),
                            )
