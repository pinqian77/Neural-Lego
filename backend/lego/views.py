from django.http import HttpResponse, JsonResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import os
import time
import json
import backend.settings as settings
from django.core import serializers

from django.contrib.auth.models import User
from lego.models import Comment, Data, Project, Users_data, Users_project, Users_template
from lego.permissions import IsOwnerOrReadOnly
from django.http import Http404

# Create your views here.
# status: 
# data: 

def welcome(request):
    return render(request, "index.html")

# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx"，"next_url":"/project"， }

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if user is not None and user.is_active:
            return JsonResponse({'status':200, 'uid': user.pk})

    return JsonResponse({'status': 404}, safe=False)


# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx", "next_url":"/login"，}
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        isHave = User.objects.get(username = username)

        if isHave is None and username is not None and password is not None:
            user = User.objects.create_user(username=username, password = password)
            user.is_active = True
            user.save
            return JsonResponse({'status':200})
        else:
            return JsonResponse({'status':500})

    return JsonResponse({'status': 404}, safe=False)


# Back
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素
def projectPage(request, pk):
#    context = {'status': 200,
#               'project_detail': [{"project_ID": "1", "project_name": "name", "project_time": "time"},
#                                  {"project_ID": "2", "project_name": "name", "project_time": "time"}]
#               }
    project = Users_project.objects.filter(user_id=pk)
    project = project.values('project_id')
    project = Project.objects.filter(project_id__in = project)
    context = {}
    context['project_detail'] = serializers.serialize('json', project, fields = ('project_id', 'last_save_time', 'project_name', 'is_public', 'star'))
    context['project_detail'] = json.loads(context['project_detail'])
    List = []
    for item in context['project_detail']:
        item["fields"]["project_id"] = item['pk']
        List.append(item['fields'])
    context['project_detail'] = List
    context['status'] = 200
    return JsonResponse(context, safe=False)
    # return JsonResponse(context, json_dumps_params={"ensure_ascii": False})


# Front
# POST: {"page_name":"xxx", "keyword":"xxxxx"}
def search(request, pk=None):
#    context = {'project_detail': {"project_ID": "1",
#                                  "project_name": "name", "project_time": "time"}}
    if pk is not None:
        project = Users_project.objects.filter(user_id=pk,user_id__contains = request.POST.get("keyword"))
    else:
        project = Users_project.objects.filter(is_public = True, project_name__contains = request.POST.get("keyword"))
    context = {'status': 200, "project_detail": list(project)}
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
    save_path = os.path.join(settings.MEDIA_ROOT, str(pk), request.POST.get("name"))

    project_list = Users_project.objects.filter(user_id=pk)
    is_save = False
    for item in project_list.all():
        project_name = Project.objects.get(project_id = item.project_id).project_name
        is_save = (project_name == request.POST.get("name"))
        if is_save is not False:
            break

    project = Project.objects.create(project_name=request.POST.get("name"), project_directory=save_path, is_public=request.POST.get("is_public"), star = 0)
    
    if project is None or is_save is not False:
        status = 400
    else:
        project.save()
        userProject = Users_project.objects.create(project_id = project.project_id, user_id=pk)
        userProject.save()
        status = 200
    return JsonResponse({'status':status}, safe=False)


# 现在文件是都存在一个media的文件夹下。
# 之后应该是根据用户id分别有文件夹， request.COOKIES.get(' ')来得到用户id
def uploadProject(request, pk):
    file = request.FILES['file']
    if file is None:
        return JsonResponse({"status":400})
    name = file.name
    save_path = os.path.join(settings.MEDIA_ROOT, str(pk), "project", name)

    project_list = Users_project.objects.filter(user_id=pk)
    is_save = False
    for item in project_list.all():
        project_name = Project.objects.get(project_id = item.project_id).project_name
        is_save = (project_name == name)
        if is_save is not False:
            break

    project = Project.objects.create(project_name=name, project_directory=save_path, is_public=True, star = 0)

    if project is None or is_save is not False:
        status = 400
    else:
        project.save()
        userProject = Users_project.objects.create(project_id = project.project_id, user_id=pk)
        userProject.save()
        print("save")
        status = 200
    print(is_save)
    print(save_path)

    try:
        os.makedirs(save_path)
    except Exception:
        return JsonResponse({'status':500})

    # save file
    file_path = os.path.join(save_path, str(project.project_id)+".json")
    with open(file_path, 'wb+') as fp:
        for chunk in file.chunks():
            fp.write(chunk)

    context = {"status": status}
    return JsonResponse(context, safe=False)

# Front
# POST: {"project_ID":"xxx"}
# TODO: 文件要先打包成zip
def downloadProject(request, pk):
    project_ID = request.POST.get("project_ID")
    project_path = Project.objects.only('project_directory').filter(project_id = project_ID)
    if project_path:
        try:
            response = StreamingHttpResponse(open(project_path, 'rb'))
            response["Content-type"] = "application/zip"
        except Exception as e:
            raise Http404('Invalid file')
        project_name = "placeholder"
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(project_name)
        return response
    else:
        raise Http404("Invalid file")


def profilePage(request, pk):
    context = {"name": "username"}
    return JsonResponse(context, safe=False)


# Front
# POST: {"canvas_data":"xxx"}
def canvasPage(request, pk):
    project_ID = request.POST.get("project_ID")
    project_path = Project.objects.only('project_directory').filter(project_id = project_ID)
    project_name = "placeholder"
    context = {"canvas_data": "username"}
    return JsonResponse(context, safe=False)

# TODO 检查文件合法
def canvasSave(request, pk):
    if request.method == "POST":
        file = request.FILES['file']

        if not file:
            return HttpResponse("file not find")

        save_path = os.path.join(settings.MEDIA_ROOT, pk, "project", file.name)

        # save file
        file_path = os.path.join(save_path, file.name)
        with open(file_path, 'wb+') as fp:
            for chunk in file.chunks():
                fp.write(chunk)

    context = {"isSave": True}
    return JsonResponse(context, safe=False)

# 传一个string 需要前端自己分词，还是说我这边分号，传很多个参数过来, 如果是后一种，将这里的context修改为想要的参数，左边为自己想要的名字


# Front
# POST: {"optimizer":"xxx", "dataset":"xxx", "lr":"xxx", "t_batch_size":"xxx", "batch_size":"xxx", "epoch":"xxx", "seed"="xxx"}
def trainPage(request, pk):
    project_ID = request.POST.get("project_ID")
    project_path = Project.objects.only('project_directory').filter(project_id = project_ID)
    project_json_name = project_ID + ".json"
    with open(os.path.join(project_path, project_json_name), 'r') as f:
        context = json.load(f)
    return JsonResponse(context, safe=False)


def trainSave(request, pk):
    project_ID = request.POST.get("project_ID")
    project_path = Project.objects.only('project_directory').filter(project_id = project_ID)
    project_json_name = project_ID + ".json"
    project_json = request.POST.get("project_json")
    with open(os.path.join(project_path, project_json_name), 'w') as f:
        json.dump(project_json, f)
    context = {"isSave": True}
    return JsonResponse(context, safe=False)


def trainRun(request, pk):
    context = {"isRun": True}
    return JsonResponse(context, safe=False)


# Front
# POST: 还不是很清楚
def uploadDataset(request, pk):
    if request.method == "POST":
        file = request.FILES['file']

        if not file:
            return HttpResponse("file not find")

        save_path = os.path.join(settings.MEDIA_ROOT, pk, "project", file.name)
        try:
            os.makedirs(save_path)
        except Exception:
            raise Http404("Invalid file")

        # save file
        file_path = os.path.join(save_path, file.name+".json")
        with open(file_path, 'wb+') as fp:
            for chunk in file.chunks():
                fp.write(chunk)

    context = {"isUpload": True}
    return JsonResponse(context, safe=False)
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素


def templatePage(request, pk):
    context = {'project_share': {"project_ID": "1", "project_name": "name", "project_time": "time"}, 'project_recommend': {
        "project_ID": "1", "project_name": "name", "project_time": "time"}, 'starlist': [1, 2, 3, 4]}

    project = Project.objects.filter(is_public=True).order_by(star)
    context = {'status': 400, 'project_list': list(project)}
    return JsonResponse(context, safe=False)


def templateStar(request, pk):
    project_ID = request.POST.get("project_ID")
    user_ID = request.POST.get("User_ID")
    project = Project.objects.get(project_id=project_ID)
    project.star += 1
    project.save()
    userProject = Users_template(project_id=project_ID, user_id=user_ID)
    userProject.save()
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

