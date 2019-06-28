from django.contrib import admin
from django.urls import path
from .views import post_list,post_details,post_share,post_search
from .feeds import LatestPostFeed

app_name='blog'

urlpatterns = [
    path('list/',post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_details,name='post_details'),
    path('share/<int:post_id>',post_share,name='post_share'),
    path('list/<slug:tag_slug>',post_list,name='post_list_with_tags'),
    path('feed/',LatestPostFeed(),name='post_feed'),
    path('search/',post_search,name='post_search'),
]
