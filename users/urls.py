from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_user', views.CreateUser.as_view(), name='create_user')
]