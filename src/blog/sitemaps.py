from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSiteMap(Sitemap):
    changefreq='weekly'
    priority=0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self,item):
        return item.updated
