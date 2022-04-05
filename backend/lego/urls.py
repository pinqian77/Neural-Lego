from django.urls import path

from . import views

# 'x/' is defined by frontend in src/router/index.js, 'views.x' is defined by backend in lego/views.py
urlpatterns = [
    path('', views.welcome),

    path('login/', views.login),
    path('register/', views.register),

    path('project/', views.projectPage),

    path('profile/', views.profilePage),

    path('train/', views.trainPage),

    path('canvas/', views.canvasPage),

]
