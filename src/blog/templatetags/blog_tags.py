from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.all().count()

@register.inclusion_tag('latest_posts.html')
def latest_posts(count=3):
    posts=Post.objects.all().order_by('-publish')[:count]
    return {'latest_posts':posts}

@register.simple_tag
def most_commented(count=5):
    most_commented_posts=Post.objects.all().annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    print("Here are the required posts")
    print(most_commented_posts)
    return most_commented_posts

@register.filter()
def markdown_convert(text):
    return mark_safe(markdown.markdown(text))    
