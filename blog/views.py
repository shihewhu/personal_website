from django.shortcuts import render
from blog.models import Post
# Create your views here.


def index(request):
    post_sorted_by_date_top_4 = Post.objects.order_by('-posted')
    if len(post_sorted_by_date_top_4) > 4:
        post_sorted_by_date_top_10 = post_sorted_by_date_top_4[:4]
    return render(request, 'blog/index.html', {'posts': post_sorted_by_date_top_4})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def blog(request):
    return render(request, 'blog/blog_homepage.html')


def post(request, postID):
    """
    view for post
    :param request:
    :param postID:
    :return:
    """
    post = Post.objects.get(id=postID)
    return render(request, 'blog/post.html', {'post': post})

