from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^blog/$', views.blog),
    url(r'^blog/post/(?P<postID>[0-9]+)', views.post)
]