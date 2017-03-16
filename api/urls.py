from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^samples/$', views.sample_list),
    url(r'^samples/(?P<pk>[0-9]+)$', views.sample_detail),
    url(r'^sample/new', views.new_sample),
    url(r'^sample/delete/(?P<pk>[0-9]+)$', views.delete_sample),
]
