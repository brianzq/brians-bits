from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.urls import reverse
from mysite.apps.projects.models import Project

# Create your views here.
class ProjectDetailView(DetailView):
    model = Project


class ProjectDetailRedirect(RedirectView):
    def get_redirect_url(self, pk):
        project = Project.objects.get(pk=pk)
        slug = project.slug
        return reverse('project', args=(pk, slug))
