from django.conf.urls import url, include
from . import views
from django.contrib import  admin
from django.contrib.auth.views import login, logout



urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/post/logged_out'}, name='logout'),
    url(r'^logged_out/$', views.logged_out, name="logout_page"),
    url(r'^add/$', views.add_new_post, name='add'),
    url(r'^board/$', views.add_new_post, name='board')

]

