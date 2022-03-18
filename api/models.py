from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime
from string import ascii_lowercase, ascii_uppercase, digits
from random import choices


class Url(models.Model):
    full_url = models.URLField(max_length=255, verbose_name="Полный url")
    short_url = models.SlugField(max_length=10, db_index=True, verbose_name="Короткий url")
    last_redirect = models.DateField(null=True, verbose_name="Дата последнего перехода по ссылке")

    def __str__(self):
        return self.full_url

    def generate_short_url(self):
        flag = True
        while flag:
            url = ''.join(choices(ascii_lowercase + ascii_uppercase + digits, k=6))
            try:
                Url.objects.get(short_url=url)
            except Url.DoesNotExist:
                self.short_url = url
                flag = False

    def redirect_time_now(self):
        self.last_redirect = datetime.now()
