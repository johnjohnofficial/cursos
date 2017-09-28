# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from news_app.models import News

# Create your views here.
def home(request):
	# return HttpResponse("<h1>Hello World!</h1>")

	menus = [
		'Home',
		'Menu #1',
		'Menu #2',
		'Menu #3',
		'Menu #4',
		'Menu #5',
		'Menu #6',
		'Menu #7',
		'Menu #8',
	]

	name_company = 'Project name'

	context = {
		'name_company': name_company,
		'menus': menus,
		'rodape': '© 2017 Company, Inc.'
	}

	news = News()
	news.title('Show News #1')
	news.content('### content ###')
	news.status('Published')
	news.save()

	return render(request, 'cms/home.html', context)