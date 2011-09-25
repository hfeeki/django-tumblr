from django.contrib import admin
from django_tumblog_proj.apps.tumblog.blog.models import Post, Link, Quote

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = { "urltitle": ("title",)}

class LinkAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Quote)
