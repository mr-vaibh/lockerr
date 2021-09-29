from django.db import models

from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

# Create your models here.

class LongUrl(models.Model):
    slug = models.SlugField(max_length=200, unique=True, default='')
    url = models.URLField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(get_random_string(length=16))
        super(LongUrl, self).save(*args, **kwargs)