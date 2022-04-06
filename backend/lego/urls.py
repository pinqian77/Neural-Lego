from django.urls import path

from . import views

# 'x/' is defined by frontend, 'views.x' is defined by backend
# frontend SEND DATA TO 'x/';
# backend SEND DATA BY 'views.x'
urlpatterns = [
    path('', views.welcome),

    path('login/', views.login),
    path('register/', views.register),

    path('project/', views.projectPage),
    path('project/upload/', views.getProjectFile),
    path('project/search/', views.search),

    path('profile/', views.profilePage),

    path('train/', views.trainPage),

    path('canvas/', views.canvasPage),

]
