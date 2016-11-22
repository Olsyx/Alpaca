from django.conf.urls import url

from . import views

app_name = "alpaca"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/(?P<activity_id>[0-9]*)$', views.signup, name='signup'),
    url(r'^login/(?P<activity_id>[0-9]*)$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^activity/(?P<activity_id>[0-9]+)$', views.activity, name='activity'),
    url(r'^activity/join/(?P<activity_id>[0-9]+)$', views.join_activity, name='join_activity'),
    url(r'^activity/leave/(?P<activity_id>[0-9]+)$', views.leave_activity, name='leave_activity'),
    url(r'^activity/confirm/(?P<activity_id>[0-9]+)$', views.confirm_session, name='confirm_session'),
    url(r'^activity/kick/(?P<activity_id>[0-9]+)$', views.kick_attendant, name='kick_attendant'),
    url(r'^activity/waitlist/(?P<activity_id>[0-9]+)$', views.waitlist, name='waitlist')
]