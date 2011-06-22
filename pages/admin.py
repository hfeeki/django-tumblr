from django.contrib import admin
from tumblog.pages.models import Page

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug": ("title",)}

admin.site.register(Page, PageAdmin)