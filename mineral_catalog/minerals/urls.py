from django.urls import path

from django.conf.urls import url, include
from minerals import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url('^mineral_list/(?P<refine>\w+)/$', views.mineral_list, name='mineral_list'),
    url(r'^mineral_detail/(?P<pk>\d+)/(?P<name>\w+)/$', views.mineral_detail, name='detail')
]
