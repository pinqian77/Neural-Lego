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

    path('login/', views.login, name="login"),
    path('register/', views.register, name = 'register'),

    path('project/<int:pk>/', views.projectPage, name = 'projectPage'),
    path('project/upload/<int:pk>/', views.uploadProject,name = 'uploadProject'),
    path('project/search/<int:pk>/', views.search, name = 'search'),

    path('profile/<int:pk>/', views.profilePage, name = 'profilePage'),

    path('train/<int:pk>/', views.trainPage, name = 'trainPage'),

    path('canvas/<int:pk>', views.canvasPage, name = 'canvasPage'),

]
