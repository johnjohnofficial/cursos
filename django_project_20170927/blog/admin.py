# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'status')
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
