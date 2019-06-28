from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from .forms import SharePostForm,NewCommentForm,SearchPostForm
from django.urls import reverse
from django.core.mail import send_mail
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector



# Create your views here.

def post_list(request,tag_slug=None):
    posts=Post.objects.all()
    tags=Post.tag.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=Post.objects.filter(tag=tag)
        print(posts)



    return render(request,'blog/list.html',{'posts':posts,'tags':tags,'tag':tag})

def post_details(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    comments=Comment.objects.filter(post=post)
    similar_posts=post.tag.similar_objects()
    print(similar_posts)
    if request.method=='POST':
        form=NewCommentForm(request.POST)
        if form.is_valid:
            print(form)

            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        form=NewCommentForm()
    return render(request,'blog/detail.html',{'post':post,'form':form,'comments':comments,'similar_posts':similar_posts})

def post_share(request,post_id):
    sent=False
    post=get_object_or_404(Post,id=post_id)
    if(request.method =='POST'):
        form=SharePostForm(request.POST)
        if(form.is_valid()):
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject = "{} recommends you to read {} by {}".format(cd['name'],post.title,post.author)
            message="{} is an excellent read.Please make sure to go through it once.Here is the link to the post : {}".format(post.title,post_url)
            sent =True
            send_mail(subject,message,'animetech25@gmail.com',[cd['to']])
            # print(request.build_absolute_uri(post.get_absolute_url()))
    else:
        form=SharePostForm()

    return render(request,"blog/share.html",{'form':form,'sent':sent})


def home(request):
    return render(request,'base.html')


def post_search(request):

    form=SearchPostForm()
    keyword=None
    posts=[]
    if('keyword' in request.GET):

        form=SearchPostForm(request.GET)
        if form.is_valid():
            cd=form.cleaned_data
            keyword=cd['keyword']
            posts=Post.objects.annotate(search=SearchVector('title','body')).filter(search=keyword)
    #
    # else:
    #         form=SearchPostForm()

    return render(request,'blog/search.html',{'form':form,'posts':posts,'keyword':keyword})
