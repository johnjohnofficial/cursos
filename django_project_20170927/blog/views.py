# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Category, Post
from blog.models import Post


# Create your views here.
def home(request):

    name = 'JohnJohn'

    # languages = ['Python', 'PHP', 'Shell Script', 'Java', 'C', 'Perl']
    #
    # for language in languages:
    #     Category.objects.create(name=language)

    all_categories = Category.objects.all()

    # category_python = Category.objects.get(name='Java')

    # post = Post.objects.get(pk=1)

    posts = Post.objects.filter(status='Published')

    # post = Post()
    # post.name = 'Post #4'
    # post.content = 'Content'
    # post.status = 'Published'
    # post.category = category_python
    # post.save()

    # post_delete = Post.objects.get(pk=2)
    # post_delete.delete()

    context = {
        'name': name,
        'categories': all_categories,
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def show_by_category(request, category_id):
    all_categories = Category.objects.all()

    category = Category.objects.get(pk=category_id)

    posts = Post.objects.filter(category=category, status='Published')

    context = {
        'categories': all_categories,
        'category': category,
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)
