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

	category_python = Category.objects.get(name='Ruby')

	post = Post()
	post.name = 'Show Post 7'	
	post.content = "content"
	post.status = "Draft"
	post.category = category_python
	post.save()

	posts = Post.objects.filter(status='Published')


	context = {
		'name': name,
		'categories': all_categories,
		'posts':posts,
	}

	return render(request, 'blog/home.html', context)

def show_post_by_category(request, category_id):

	name = "João"

	all_categories = Category.objects.all()

	category = Category.objects.get(pk=category_id)

	posts = Post.objects.filter(category=category, status='Published')

	context = {
		'name': name,
		'categories': all_categories,
		'posts': posts,
	}

	return render(request, 'blog/home.html', context)