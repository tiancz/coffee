from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDict

from .forms import CommentForm

from django.urls import reverse
from django.views import generic

from .models import Blog,Comment,Category,Tag

# Create your views here.



def get_all_blogs(request):

	blogs_list = Blog.objects.all().order_by('-created')
	paginator = Paginator(blogs_list,3)

	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer,deliver first page.
		blogs = paginator.page(1)
	except EmptyPage:
		#if page is out of range(eg. 9999),deliver last page of results.
		blogs = paginator.page(paginator.num_pages)
	return render(request,'blog/index.html',{'blogs':blogs})


def get_blog_by_id(request,blog_id):

	blog = get_object_or_404(Blog,id=blog_id)
	if request.method == 'GET':
		form = CommentForm()
	else:
		form = CommentForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			cleaned_data['blog'] = blog
			Comment.objects.create(**cleaned_data)
	ctx = {
		'blog':blog,
		'comments':blog.comment_set.all().order_by('-created'),
		'form':form

	}

	return render(request,'blog/blog-detail.html',ctx)

def archive(request):
	blogs_list = Blog.objects.all().order_by('-created')
	blogs_date = Blog.objects.datetimes('created','month',order='DESC')
	return render(request,'blog/blog-archive.html',{'blogs':blogs_list,'date':blogs_date})

def category(request):
	blogs_list = Blog.objects.all().order_by('-created')
	blogs_category = Category.objects.all().distinct()
	return render(request,'blog/blog-category.html',{'blogs':blogs_list,'categorys':blogs_category})

def tags(request):
	blogs_list = Blog.objects.all().order_by('-created')
	blogs_tag = Tag.objects.all()
	return render(request,'blog/blog-tags.html',{'blogs':blogs_list,'tags':blogs_tag})

def about(request):
	return render(request,'blog/about.html','')

