from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.first_app, name='main-view'),
    path('viewlist.html', views.viewlist, name='viewlist')
]