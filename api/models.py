import uuid

from django.conf import settings
from django.db import models


class Link(models.Model):
    source_link = models.URLField()
    short_link = models.URLField(default=f'{settings.HOST_URL}/{uuid.uuid4().hex[:6]}',
                                 unique=True)
    created_at = models.DateTimeField(auto_now=True)
