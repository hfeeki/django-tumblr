from django.contrib import admin
from django_tumblog_proj.apps.pages.models import Page

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug": ("title",)}

admin.site.register(Page, PageAdmin)