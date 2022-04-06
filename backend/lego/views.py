import json
import os
from urllib import response
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect, render

import backend.settings as settings

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
        return redirect(next_url)

    context = {'isLogin': True}
    return render(request, "index.html", context)


# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx", "next_url":"/login"，}
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next_url")
        return redirect(next_url)

    context = {'isLogin': True}
    return render(request, "index.html", context)


# Back
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素
def projectPage(request):
    context = {'project_detail': [{"project_ID": "1", "project_name": "name", "project_time": "time"},
                                  {"project_ID": "2", "project_name": "name", "project_time": "time"}]
               }
    return render(request, "index.html", context)


# Front
# POST: {"page_name":"xxx", "keyword":"xxxxx"}
def search(request):
    context = {'project_detail': {"project_ID": "1",
                                  "project_name": "name", "project_time": "time"}}
    return render(request, "index.html", context)


# Front
# POST: {"project_ID":"1"}
def deleteProject(request):
    context = {"isDelete": True}
    return render(request, "index.html", context)


# Front
# POST: {"project_name":"xxx", "project_time":"time"}
def newProject(request):
    context = {"isNew": True}
    return render(request, "index.html", context)


# 现在文件是都存在一个media的文件夹下。
# 之后应该是根据用户id分别有文件夹， request.COOKIES.get(' ')来得到用户id
def getProjectFile(request):
    if request.method == "POST":
        file = request.FILES['file']

        if not file:
            print("file not find")
            return HttpResponse("file not find")

        save_path = os.path.join(settings.MEDIA_ROOT, file.name)
        try:
            print("making media dir...")
            os.mkdir(settings.MEDIA_ROOT)
        except Exception:
            pass

        # save file
        print("start to save file...")
        with open(save_path, 'wb+') as fp:
            for chunk in file.chunks():
                fp.write(chunk)

        print("save file done...")

        return HttpResponse("upload ok!")
        # context = {"isUpload": True}
        # return render(request, "index.html", context)


# Front
# POST: {"project_ID":"xxx"}
# TODO: 这个页面我数据库还没建，具体要什么信息确认后，建立数据库
def downloadProject(request):
    response = StreamingHttpResponse("hi")
    return response


def profilePage(request):
    context = {"name": "username"}
    return render(request, "index.html", context)


# Front
# POST: {"canvas_data":"xxx"}
def canvasPage(request):
    if request.method == "POST":
        # file = request.POST.get("file")
        file = json.loads(request.body)
        print(file)
        return HttpResponse("hhhhh")
    context = {"file": "name", "python": "name"}
    return render(request, "index.html", context)


def canvasSave(request):
    context = {"isSave": True}
    return render(request, "index.html", context)

# 传一个string 需要前端自己分词，还是说我这边分号，传很多个参数过来, 如果是后一种，将这里的context修改为想要的参数，左边为自己想要的名字


# Front
# POST: {"optimizer":"xxx", "dataset":"xxx", "lr":"xxx", "t_batch_size":"xxx", "batch_size":"xxx", "epoch":"xxx", "seed"="xxx"}
def trainPage(request):
    context = {"hyperpars": "name"}
    return render(request, "index.html", context)


def trainSave(request):
    context = {"isSave": True}
    return render(request, "index.html", context)


def trainRun(request):
    context = {"isRun": True}
    return render(request, "index.html", context)


# Front
# POST: 还不是很清楚
def uploadDataset(request):
    context = {"isUpload": True}
    return render(request, "index.html", context)
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素


def templatePage(request):
    context = {'project_share': {"project_ID": "1", "project_name": "name", "project_time": "time"}, 'project_recommend': {
        "project_ID": "1", "project_name": "name", "project_time": "time"}, 'starlist': [1, 2, 3, 4]}
    return render(request, "index.html", context)


def templateStar(request):
    context = {'isStar': True}
    return render(request, "index.html", context)


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
