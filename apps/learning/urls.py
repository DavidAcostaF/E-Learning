
from django.urls import path

from . import views

urlpatterns = [
    path('',views.MyClass.as_view(),name = 'home'),
    path('create_classroom/',views.CreateClasroom.as_view(),name='create_classroom'),
    path('join_in_classroom/',views.JoinInClass.as_view(),name='join_classroom'),
    path('classroom/<slug:classroom_code>/',views.DetailClassroom.as_view(),name='detail_classroom'),

    path('create_post/<str:slug>/',views.CreateActivity.as_view(),name='create_post'),
    path('activity/<int:pk>/',views.DetailActivity.as_view(),name='activity'),
    path('classroom/delete_activity/<int:pk>/',views.DeleteActivity.as_view(),name='delete_activity'),
    path('classroom/submit_activity/<int:pk>/',views.SubmitActivity.as_view(),name='submit_activity'),
    path('classroom/cancel_submit/<int:pk>/',views.CancelSubmit.as_view(),name='cancel_submit')

]