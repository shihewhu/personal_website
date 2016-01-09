from django.db import models
from django.db.models import permalink
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, default="")
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return '{}'.format(self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '{}'.format(self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})





class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    blog = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_comment', None, {'slug': self.slug})
