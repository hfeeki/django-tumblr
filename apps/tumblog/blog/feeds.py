from django.contrib.syndication.views import Feed
from django_tumblog_proj.apps.tumblog.blog.models import Post, Link, Quote, Photo, Video
from django_tumblog_proj.apps.tumblog.entries.models import TumbleItem

class BlogPostFeed(Feed):
    title = "WillVanWazer.com latest blog entries"
    link = "/feed/"
    description = "The latest blog entires posted on WillVanWazer.com"

    def items(self):
        return Post.objects.order_by('-date')[:15]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.post

class AllItemsFeed(Feed):
    title = "WillVanWazer.com all items feed"
    link = "/feed/allitems"
    description = "ALL THE THINGS!!!!"

    def items(self):
        return TumbleItem.objects.order_by('-pub_date')[:15]

    def item_title(self, item):
        if item.content_type.name == "quote":
            return item.content_object.quote
        else:
            return item.content_object.title

    def item_description(self, item):
        return "Test"

    def item_link(self, item):
        return "http://willvanwazer.com%s" % item.content_object.get_absolute_url()
