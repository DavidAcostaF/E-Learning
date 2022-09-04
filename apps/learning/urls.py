
from django.urls import path

from . import views

urlpatterns = [
    path('',views.tem.as_view(),name = 'index')
]