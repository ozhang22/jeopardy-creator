from django.conf.urls import url

from . import views

app_name = 'creator'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameView.as_view(), name='game'),
]
