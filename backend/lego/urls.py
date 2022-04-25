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

    path('project/<int:pk>/', views.projectPage),
    path('project/create/<int:pk>/', views.newProject),
    path('project/upload/<int:pk>/', views.uploadProject),
    path('project/search/<int:pk>/', views.search),
    path('project/remove/<int:pk>/<int:pid>/', views.deleteProject),
    path('project/download/<int:pk>/<int:pid>/', views.downloadProject),

    path('dataset/<int:pk>/', views.dataPage),
    path('dataset/upload/<int:pk>/', views.uploadDataset),
    path('dataset/remove/<int:pk>/<int:did>/', views.deleteData),

    path('profile/<int:pk>/', views.profilePage),

    path('train/<int:pk>/<int:pid>/', views.trainPage),
    path('train/apply/<int:pk>/<int:pid>/', views.trainSave),
    path('train/run/<int:pk>/<int:pid>/', views.trainRun),
    path('train/status/<int:pk>/<int:pid>/', views.trainStatus),
    path('train/roc/<int:pk>/<int:pid>/', views.trainROC),
    path('train/acc/<int:pk>/<int:pid>/', views.trainACC),
    path('train/epoch/<int:pk>/<int:pid>/', views.trainEpoch),


    path('canvas/getPython/<int:pk>/<int:pid>/', views.canvasPython),
    path('canvas/getJson/<int:pk>/<int:pid>/', views.canvasJson),
    path('canvas/compile/<int:pk>/<int:pid>/', views.canvasSave),
]
