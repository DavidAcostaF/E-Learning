
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.tem.as_view(),name = 'index'),
    path('create_classroom/',views.CreateClasroom.as_view(),name='create_classroom'),
    path('join_in_classroom/',views.JoinInClass.as_view(),name='join_classroom')
]