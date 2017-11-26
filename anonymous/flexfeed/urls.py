from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^login/$', views.login, name='login'),
    url(r'^discovery/$', views.discover, name='discover'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^groups/edit/$', views.edit, name='edit')
]

urlpatterns += [
    url(r'^editprofile/', views.edit_Profile, name='editprofile'),
]

# url mapping for editing specific groups
urlpatterns += [
    url(r'^groups/edit_group(?:/(?P<pk>[-\w]+))?/$', views.edit_group, name='edit_group'),

]