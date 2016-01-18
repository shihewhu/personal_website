from django.contrib import admin
from blog.models import Post, Comment, Tag, Introduction, Contact_information
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Introduction)
admin.site.register(Contact_information)
