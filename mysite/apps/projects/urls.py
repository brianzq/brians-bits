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
from mysite.apps.projects.models import Project
from mysite.apps.projects.views import ProjectDetailView, ProjectDetailRedirect


urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Project.objects.all().order_by('-pub_date')[:25],
                         template_name='projects/projects-index.html')),
    url(r'^(?P<pk>\d+)/?$',
        ProjectDetailRedirect.as_view(), name='project'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/?$',
        ProjectDetailView.as_view(template_name='projects/project.html'), name='project'),
]
