from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView

from api.models import Url


class Redirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = get_object_or_404(Url, short_url=kwargs['short_url'])
        url.redirect_time_now()
        url.save()
        return url.full_url


class IndexView(TemplateView):
    template_name = 'index.html'
