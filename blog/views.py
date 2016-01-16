from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post, Tag, Introduction
from blog.forms import ContactForm
# Create your views here.


def index(request):
    post_sorted_by_date_top_4 = Post.objects.all().order_by('-posted')[:4]
    introduction = Introduction.objects.first()
    return render(request, 'blog/index.html', {'post_list': post_sorted_by_date_top_4,
                                               'introduction': introduction})


def about(request):
    introduction = Introduction.objects.first()
    return render(request, 'blog/about.html', {'introduction': introduction})


def contact(request):
    if request.method == "POST":
        contact_form= ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/blog/thanks')
    else:
        contact_form = ContactForm()
        return render(request, 'blog/contact.html', {'contact_form': contact_form})

def thanks(request):
    return  render(request, 'blog/thanks.html')

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

