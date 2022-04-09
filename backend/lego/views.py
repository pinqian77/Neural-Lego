from django.http import HttpResponse, JsonResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os
import time

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from lego.models import Comment, Data, Project, Users_data, Users_project, Users_template
from lego.serializers import CommentSerializer, DataSerializer, ProjectSerializer, UserDataSerializer, UserProjectSerializer, UserSerializer, UserTemplateSerializer
from lego.permissions import IsOwnerOrReadOnly
from django.http import Http404


# Create your views here.

def welcome(request):
    return render(request, "index.html")

# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx"，"next_url":"/project"， }


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next_url")

        user = authenticate(username = username, password = password)
        if user is not None and user.is_active:
            return redirect(next_url)

    context = {'isLogin': True}
    return JsonResponse(context, safe=False)


# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx", "next_url":"/login"，}
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username is not None and password is not None:
            user = User.objects.create_user(username=username, password = password)
            user.is_active = True
            user.save
            return redirect(request.POST.get("next_url"))

    context = {'isLogin': True}
    return JsonResponse(context, safe=False)


# Back
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素
def projectPage(request, pk):
#    context = {'status': 200,
#               'project_detail': [{"project_ID": "1", "project_name": "name", "project_time": "time"},
#                                  {"project_ID": "2", "project_name": "name", "project_time": "time"}]
#               }
    project = Users_project.objects.filter(user_id=pk)
    project = list(project)
    context = {'status': 200, 'project_detail': project}
    return JsonResponse(context, safe=False)
    # return JsonResponse(context, json_dumps_params={"ensure_ascii": False})


# Front
# POST: {"page_name":"xxx", "keyword":"xxxxx"}
def search(request, pk=None):
#    context = {'project_detail': {"project_ID": "1",
#                                  "project_name": "name", "project_time": "time"}}
    if pk is not None:
        project = Users_project.objects.filter(user_id=pk,project_name__contains = request.POST.get("keyword"))
    else:
        project = Users_project.objects.filter(is_public = True, project_name__contains = request.POST.get("keyword"))
    context = {"project_detail": list(project)}
    return JsonResponse(context, safe=False)


# Front
# POST: {"project_ID":"1"}
# TODO: 删掉这个的地址的文件
def deleteProject(request, pk):
    project = Users_project.objects.get(project_id=request.POST.get("project_ID"), user_id = pk)
    if project is None:
        context = {"isDelete": False, "error": "Invalid project"}
    else:
        context = {"isDelete": True, "error": None}
    return JsonResponse(context, safe=False)


# Front
# POST: {"project_name":"xxx", "project_time":"time"}
# TODO: 真的存这个文件夹， 要前端发送is_public过来
def newProject(request, pk):
    project = Project(project_name=request.POST.get("project_name"), project_directory=os.path.join('.','media',pk ,request.POST.get("project_name")), last_save_time=time.localtime(),is_public=request.POST.get("is_public"))
    if project is None:
        context = {"isDelete": False, "error": "Invalid project"}
    else:
        project.save()
        context = {"isDelete": True, "error": None}
    return JsonResponse(context, safe=False)


# 现在文件是都存在一个media的文件夹下。
# 之后应该是根据用户id分别有文件夹， request.COOKIES.get(' ')来得到用户id
def uploadProject(request):
    context = {"isNew": True}
    return JsonResponse(context, safe=False)

# Front
# POST: {"project_ID":"xxx"}
# TODO: 这个页面我数据库还没建，具体要什么信息确认后，建立数据库
def downloadProject(request):
    response = StreamingHttpResponse("hi")
    return response


def profilePage(request):
    context = {"name": "username"}
    return JsonResponse(context, safe=False)


# Front
# POST: {"canvas_data":"xxx"}
def canvasPage(request):
    context = {"canvas_data": "username"}
    return JsonResponse(context, safe=False)

def canvasSave(request):
    context = {"isSave": True}
    return JsonResponse(context, safe=False)

# 传一个string 需要前端自己分词，还是说我这边分号，传很多个参数过来, 如果是后一种，将这里的context修改为想要的参数，左边为自己想要的名字


# Front
# POST: {"optimizer":"xxx", "dataset":"xxx", "lr":"xxx", "t_batch_size":"xxx", "batch_size":"xxx", "epoch":"xxx", "seed"="xxx"}
def trainPage(request):
    context = {"hyperpars": "name"}
    return JsonResponse(context, safe=False)


def trainSave(request):
    context = {"isSave": True}
    return JsonResponse(context, safe=False)


def trainRun(request):
    context = {"isRun": True}
    return JsonResponse(context, safe=False)


# Front
# POST: 还不是很清楚
def uploadDataset(request):
    context = {"isUpload": True}
    return JsonResponse(context, safe=False)
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素


def templatePage(request):
    context = {'project_share': {"project_ID": "1", "project_name": "name", "project_time": "time"}, 'project_recommend': {
        "project_ID": "1", "project_name": "name", "project_time": "time"}, 'starlist': [1, 2, 3, 4]}
    return JsonResponse(context, safe=False)


def templateStar(request):
    context = {'isStar': True}
    return JsonResponse(context, safe=False)


# def getProjectFile(request):
#     file = request.FILES['file']
#     file_path = os.path.join(settings.MEDIA_ROOT, image_name)
#        # 在没有目录路径时创建一个
#        try:
#             os.mkdir(settings.MEDIA_ROOT)
#         except Exception:
#             pass
#         # 将文件保存在本地
#         f = open(image_path, 'wb')
#         for i in onecard.chunks():
#             f.write(i)
#         f.close()
#         # 创建用户
#         try:
#             UserModel.objects.create(name=name, image=image_name)
#         except Exception as e:
#             # logger.info("[Users] Fail to create user!\n", e)
#             response['success'] = '0'
#         return Response(response)

#def uploadProject(request):
#    if request.method == "POST":
#        file = request.FILES['file']
#
#        if not file:
#            print("file not find")
#            return HttpResponse("file not find")
#
#        save_path = os.path.join(settings.MEDIA_ROOT, file.name)
#        try:
#            print("making media dir...")
#            os.mkdir(settings.MEDIA_ROOT)
#        except Exception:
#            pass
#
#        # save file
#        print("start to save file...")
#        with open(save_path, 'wb+') as fp:
#            for chunk in file.chunks():
#                fp.write(chunk)
#
#        print("save file done...")
#
#        return HttpResponse("upload ok!")
        # context = {"isUpload": True}
        # return render(request, "index.html", context)

#def canvasPage(request):
#    if request.method == "POST":
#        # file = request.POST.get("file")
#        file = json.loads(request.body)
#        print(file)
#        return HttpResponse("hhhhh")
#    context = {"file": "name", "python": "name"}
#    return render(request, "index.html", context)

