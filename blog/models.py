from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '{}'.format(self.tag)

    def get_absolute_url(self):
        return '/blog/blog/tag/{}'.format(str(self.id))



class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, default="")
    background_picture = models.ImageField(upload_to='blog/static/img/', default='blog/static/img/post-bg.img')
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return '/blog/blog/post/{}'.format(str(self.id))


    def get_static_background_picture_url(self):
        garbage, true_url = str(self.background_picture.url).split('/', 1)
        return "/{}".format(true_url)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    blog = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(self.title)

