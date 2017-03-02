
from django.conf.urls import url,include

from . import views

app_name = 'blog'
urlpatterns = [
#	url(r'^$',views.index,name='index'),
	url(r'^$',views.get_all_blogs,name='index'),
#	url(r'^$',views.get_all_blogs,name='blog_list'),
	url(r'^(?P<blog_id>[0-9]+)/$',views.get_blog_by_id,name='blog_detail'),
	url(r'^archive$',views.archive,name='archive'),
	url(r'^category$',views.category,name='category'),
	url(r'^tags$',views.tags,name='tags'),
	url(r'^about$',views.about,name='about'),

]


