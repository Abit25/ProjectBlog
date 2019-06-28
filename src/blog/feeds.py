from django.contrib.syndication.views import Feed
from .models import Post

class LatestPostFeed(Feed):
    title='My Blog'
    link='/blog/'
    description='New Posts of my Blog'

    def items(self):
        return Post.objects.all()[:5]

    def item_title(self,item):
        return item.title


    def item_description(self,item):
        return item.body
