from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.home, name='blog.home'),
    url(r'category/(?P<category_id>\d+)', views.show_by_category, name='blog.show_by_category'),
]