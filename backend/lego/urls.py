from django.urls import path
#from rest_framework.routers import DefaultRouter

from . import views

#router = DefaultRouter()
#router.register('login', views.login)
#router.register('register', views.register)
#router.register('project', views.projectPage)
#router.register('project', views.projectPage)
# 'x/' is defined by frontend, 'views.x' is defined by backend
# frontend SEND DATA TO 'x/';
# backend SEND DATA BY 'views.x'
urlpatterns = [
    path('', views.welcome),

    path('login/', views.login),
    path('register/', views.register),

    path('project/', views.projectPage),
    path('project/upload/', views.uploadProject),
    path('project/search/', views.search),

    path('profile/', views.profilePage),

    path('train/', views.trainPage),

    path('canvas/', views.canvasPage),

]
