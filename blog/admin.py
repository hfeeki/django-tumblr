from django.contrib import admin
from tumblog.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = { "urltitle": ("title",)}

admin.site.register(Post, PostAdmin)