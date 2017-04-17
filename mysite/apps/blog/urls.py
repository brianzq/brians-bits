"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mysite.apps.blog.models import Post
from mysite.apps.blog.views import PostDetailView, PostDetailRedirect

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Post.objects.all().order_by('-pub_date')[:25],
                         template_name='blog/blog-index.html')),
    url(r'^(?P<pk>\d+)/?$',
        PostDetailRedirect.as_view()),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/?$',
        PostDetailView.as_view(template_name='blog/post.html'), name='post')
]
