from django.conf.urls import url
from . import views

app_name = 'registration'

urlpatterns = [
        url(r'^$', views.welcome, name='welcome'),
        url(r'^register-session/$', views.register, name='register-session'),
        url(r'^register/$', views.registerdb, name='register'),
        url(r'^confirmation/$', views.email_confirm, name='email'),
        url(r'^users/$', views.users_list, name='users'),
    ]
