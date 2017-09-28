# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    STATUS_CHOICES = (
        ('Published', 'Draft'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    dt_creation = models.DateTimeField(auto_now=True)