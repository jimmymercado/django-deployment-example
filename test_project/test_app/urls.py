from django.urls import path, re_path
from test_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='main-view'),
    re_path(r'^test', views.test, name='test'),
    re_path(r'^users.html', views.users, name='users'),
    re_path(r'^signup.html', views.signup, name='signup')
]
