from django.db import models

from string import ascii_lowercase, ascii_uppercase, digits
from random import choices


class Url(models.Model):
    full_url = models.URLField(max_length=255, verbose_name="Полный url")
    short_url = models.SlugField(max_length=10, db_index=True, verbose_name="Короткий url")

    def generate_short_url(self):
        flag = True
        while flag:
            url = ''.join(choices(ascii_lowercase + ascii_uppercase + digits, k=6))
            try:
                Url.objects.get(short_url=url)
            except Url.DoesNotExist:
                self.short_url = url
                flag = False
