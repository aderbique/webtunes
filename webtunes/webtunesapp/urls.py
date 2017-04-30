from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^success$', views.success, name='success'),
    url(r'^retrieve$', views.retrieve, name='retrieve'),
    url(r'^play$', views.play, name='play'),
    url(r'^error$', views.error, name='error'),

]