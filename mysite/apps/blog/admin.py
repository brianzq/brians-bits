from django.contrib import admin
from mysite.apps.blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
