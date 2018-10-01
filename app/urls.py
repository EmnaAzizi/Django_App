from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ayomi3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/update$', views.user_update, name='user_update'),
]
