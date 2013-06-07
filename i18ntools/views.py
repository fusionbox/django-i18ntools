from django.views.generic import RedirectView
from django.utils.http import is_safe_url

from i18ntools.utils import url_for_language


class SetLanguageView(RedirectView):
    url = '/'

    def get_next_url(self):
        """
        copied from django.views.i18n.set_language.  Grabs the next URL in a
        safe way.
        """
        next = self.request.REQUEST.get('next')
        if not is_safe_url(url=next, host=self.request.get_host()):
            next = self.request.META.get('HTTP_REFERER')
            if not is_safe_url(url=next, host=self.request.get_host()):
                next = self.url
        return next

    def get_redirect_url(self, **kwargs):
        new_language = self.request.POST.get('language', None)
        url = self.get_next_url()
        return url_for_language(url, new_language)

set_language = SetLanguageView.as_view()
