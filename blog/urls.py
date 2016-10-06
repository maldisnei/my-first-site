from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
    url(r'^blog/new/$', views.post_new, name="post_new"),
    url(r'^blog/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^drafts/$', views.post_draft_list, name="post_draft_list"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_remove, name="post_remove"),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approved'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove, name='comment_remove'),
]
