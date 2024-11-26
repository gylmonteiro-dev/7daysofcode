from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_avatars, name='lista-avatares')
]