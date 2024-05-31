from django.urls import path
from . import views


urlpatterns=[
    path('', views.getRoutes),
    path('rooms/', views.GetRoom.as_view(),name='detail'),
    path('rooms/<int:pk>/', views.Room_Detail.as_view()),
    path('user/',views.getUser),
    ]