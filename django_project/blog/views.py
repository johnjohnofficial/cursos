# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Post

# Create your views here.

def home(request):

	name = "João"
	
	# categories = ['Python', 'PHP', 'Java', 'Ruby']
	# for category in categories:
	# 	Category.objects.create(name=category)

	all_categories = Category.objects.all()

	# category_python = Category.objects.get(name='Python')

	# post = Post()
	# post.name = 'My First very Post'	
	# post.content = "Content of my first Post"
	# post.status = "Published"
	# post.category = category_python
	# post.save()

	post = Post.objects.get(pk=1)


	context = {
		'name': name,
		'categories': all_categories,
		'post':post,
	}

	return render(request, 'blog/home.html', context)