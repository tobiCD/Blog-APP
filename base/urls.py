from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.urls import path
from . import views
urlpatterns =[
    path('',views.home , name='home'),
    path('room/<int:pk>',views.room , name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<int:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<int:pk>',views.deleteRoom,name='delete-room'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.Register,name='register'),
    path('delete-message/<int:pk>', views.delete_message, name='delete-message'),
    path('profile/<int:pk>', views.userProfile, name='profile'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
    path('update-user/', views.updateUser, name='update-user'),
    path('upload-music/',views.createRoomMusic,name='upload-music')

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)