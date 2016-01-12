from django.shortcuts import render
from blog.models import Post, Tag
# Create your views here.


def index(request):
    post_sorted_by_date_top_4 = Post.objects.order_by('-posted')
    if len(post_sorted_by_date_top_4) > 4:
        post_sorted_by_date_top_4 = post_sorted_by_date_top_4[:4]
    return render(request, 'blog/index.html', {'posts': post_sorted_by_date_top_4})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def blog(request):
    """
    view for blog pages
    :param request: http request received
    :return:http response with blog_homepage.html template
    """
    tags = Tag.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog/blog_homepage.html', {'tags': tags,
                                                       'posts': posts})


def post(request, post_id):
    """
    view for post
    :param request: http request received
    :param postID: post id
    :return: http response with post.html template
    """
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post': post})

def tag(request, tag_id):
    """
    view for tag
    :param request: received http request
    :param tag: tag name
    :return: http reponse with tag.html template and tags and post objects
    """
    tag = Tag.objects.get(id=tag_id)
    posts = tag.post_set.all()
    return render(request, 'blog/tag.html', {'tag_name': tag.tag,
                                             'posts': posts})

