from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^blog/$', views.blog),
    url(r'^blog/post/(?P<post_id>[0-9]+)', views.post),
    url(r'^blog/tag/(?P<tag_id>([0-9])+)', views.tag)
]