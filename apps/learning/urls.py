
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.MyClass.as_view(),name = 'home'),
    path('create_classroom/',views.CreateClasroom.as_view(),name='create_classroom'),
    path('join_in_classroom/',views.JoinInClass.as_view(),name='join_classroom'),
    path('classroom/<slug:classroom_code>/',views.DetailClassroom.as_view(),name='detail_classroom'),

    path('create_post/<str:slug>/',views.CreatePosts.as_view(),name='create_post')
]