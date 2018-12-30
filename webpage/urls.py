from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<parameter>\S*)$', views.index, name='index'),
]
