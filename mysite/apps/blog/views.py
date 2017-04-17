from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.urls import reverse
from mysite.apps.blog.models import Post

# Create your views here.
class PostDetailView(DetailView):
    model = Post


class PostDetailRedirect(RedirectView):
    def get_redirect_url(self, pk):
        post = Post.objects.get(pk=pk)
        slug = post.slug
        return reverse('post', args=(pk, slug))
