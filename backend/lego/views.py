from django.http import HttpResponse, JsonResponse
from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import os
import time
import json
import backend.settings as settings
import zipfile
from django.core import serializers
from util.utils import main, model, cmd

from django.contrib.auth.models import User
from lego.models import Comment, Data, Project, Users_data, Users_project, Users_template
from lego.permissions import IsOwnerOrReadOnly
from django.http import Http404

# Create your views here.
# status: 
# data:{} 

def welcome(request):
    return render(request, "index.html")

# Front
# POST: {"email":"xxx@xxx.com"， "password":"xxxxxx"，"next_url":"/project"， }

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.check_password(password):
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

def querysetTojson(queryset):
    context = serializers.serialize('json', queryset)
    context = json.loads(context)
    List = []
    for item in context:
        item["fields"]["id"] = item['pk']
        List.append(item['fields'])
    return List

# Back
# 都是list {“project_ID":"1", "project_name":"name", "project_time":"time"} 表示list中的一个元素
def projectPage(request, pk):
    user = User.objects.get(pk = pk)
    project = Project.objects.filter(user_id=user)

    context = {}
    context['project_detail'] = querysetTojson(project)
    context['status'] = 200
    return JsonResponse(context, safe=False)
    # return JsonResponse(context, json_dumps_params={"ensure_ascii": False})

def dataPage(request, pk):
    user = User.objects.get(pk = pk)
    data = Data.objects.filter(user_id=user)

    context = {}
    context['dataset_detail'] = querysetTojson(data)
    context['status'] = 200
    return JsonResponse(context, safe=False)

def deleteData(request, pk, did):
    context = {}
    user = User.objects.get(pk = pk)
    data = Data.objects.get(dataset_id = did, user_id = user)
    if data is None:
        context['status'] = 500
    else:
        os.remove(data.dataset_directory)
        context['status'] = 200
    data.delete()
    return JsonResponse(context, safe=False)
# Front
# POST: {"page_name":"xxx", "keyword":"xxxxx"}
def search(request, pk=None):
#    context = {'project_detail': {"project_ID": "1",
#                                  "project_name": "name", "project_time": "time"}}
    if pk is not None:
        user = User.objects.get(pk = pk)
        project = Project.objects.filter(user_id=user, project_name__contains= request.POST.get("keyword"))
    else:
        project = Project.objects.filter(is_public = True, project_name__contains= request.POST.get("keyword"))

    context = {}
    context['project_detail'] = querysetTojson(project)
    context['status'] = 200
    return JsonResponse(context, safe=False)

# Front
# POST: {"project_ID":"1"}
# TODO: 删掉这个的地址的文件
def deleteProject(request, pk, pid):
    context = {}
    user = User.objects.get(pk = pk)
    project = Project.objects.get(project_id=pid, user_id = user)
    if project is None:
        context['status'] = 500
    else:
        for item in os.listdir(project.project_directory):
            os.remove(os.path.join(project.project_directory, item))
        os.removedirs(project.project_directory)
        context['status'] = 200
    project.delete()
    return JsonResponse(context, safe=False)

# Front
# POST: {"project_name":"xxx", "project_time":"time"}
# TODO: 真的存这个文件夹， 要前端发送is_public过来
def newProject(request, pk):
    project_name = request.POST.get("name")
    save_path = os.path.join(settings.MEDIA_ROOT, str(pk), project_name)

    user = User.objects.get(pk = pk)
    is_save = Project.objects.filter(user_id = user, project_name =project_name)

    project = Project(user_id= user, project_name=request.POST.get("name"), project_directory=save_path, is_public=request.POST.get("is_public"), star = 0)
    pid = 0
    
    if project is None or is_save.count() != 0:
        status = 400
        return JsonResponse({'status':status}, safe=False)
    else:
        project.save()
        pid = project.project_id
        status = 200

    try:
        os.makedirs(save_path)
        file = request.POST.get("file")
        file = json.loads(file)
        print("load",file)
        file_path = os.path.join(save_path, str(pid) + ".json")

        code_path = os.path.join(save_path, str(pid) + ".py")
        # save file
        with open(file_path, 'w') as fp:
            json.dump(file, fp)
        with open(code_path, 'w') as fp:
            fp.write("")
    except Exception:
        return JsonResponse({'status':500})
    return JsonResponse({'status':status}, safe=False)

# 现在文件是都存在一个media的文件夹下。
# 之后应该是根据用户id分别有文件夹， request.COOKIES.get(' ')来得到用户id
def uploadProject(request, pk):
    file = request.FILES['file']
    if file is None:
        return JsonResponse({"status":400})
    name = file.name[:-5]
    save_path = os.path.join(settings.MEDIA_ROOT, str(pk), "project", name)

    user = User.objects.get(pk = pk)

    is_save = Project.objects.filter(user_id = user, project_name = name)

    project = Project.objects.create(user_id = user, project_name=name, project_directory=save_path, is_public=True, star = 0)

    if project is None or is_save.count() != 0 :
        status = 500
    else:
        project.save()
        status = 200

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
def downloadProject(request, pk, pid):
    project_ID = pid
    project_path = Project.objects.only('project_directory').get(project_id = project_ID).project_directory

    if project_path:
        try:
            zip_dir = project_path + '.zip'
            zip_file = zipfile.ZipFile(zip_dir, 'w', zipfile.ZIP_DEFLATED)
            for item in os.listdir(project_path):
                zip_file.write(os.path.join(project_path,item))
            zip_file.close()
            response = StreamingHttpResponse(open(zip_dir, 'rb'))
            response["Content-type"] = "application/zip"
        except Exception as e:
            return JsonResponse({'status':500})
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(project_ID)
        return response
    else:
        return JsonResponse({'status':500})

def profilePage(request, pk):
    context = {"name": "username"}
    return JsonResponse(context, safe=False)

# Front
# POST: {"canvas_data":"xxx"}
def canvasPython(request, pk, pid):
    project_ID = pid
    project_path = Project.objects.only('project_directory').get(project_id = project_ID).project_directory
    model(project_path=project_path, pid=str(project_ID))
    python_path = os.path.join(project_path, "model.py")
    if python_path:
        try:
            response = StreamingHttpResponse(open(python_path, 'rb'))
            response["Content-type"] = "application/stream"
        except Exception as e:
            return JsonResponse({'status':204})

        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(project_ID)
        response["status"] = 200
        return response
    return JsonResponse({'status':204})

def canvasJson(request, pk, pid):
    project_ID = pid
    project_path = Project.objects.only('project_directory').get(project_id = project_ID).project_directory
    json_path = os.path.join(project_path, str(project_ID)+".json")
    if json_path:
        try:
            response = StreamingHttpResponse(open(json_path, 'rb'))
            response["Content-type"] = "application/json"
        except Exception as e:
            return JsonResponse({'status':204})

        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(project_ID)
        response["status"] = 200
        return response
    return JsonResponse({'status':204})

# TODO 检查文件合法
def canvasSave(request, pk, pid):
    print("\n CavbasSave\n")
    
    if request.method == "POST":

        file = request.POST.get("file")
        file = json.loads(file)
        print("file:\n",file)
        save_path = Project.objects.get(project_id=pid).project_directory

        file_path = os.path.join(save_path, str(pid) + ".json")
        # save file
        with open(file_path, 'w') as fp:
            json.dump(file, fp)

    return JsonResponse({"status":200}, safe=False)

# Front
# POST: {heper: {"optimizer":"xxx", "dataset":"xxx", "lr":"xxx", "t_batch_size":"xxx", "batch_size":"xxx", "epoch":"xxx", "seed"="xxx"}}
def trainPage(request, pk, pid):
    project_ID = pid
    project_path = Project.objects.only('project_directory').get(project_id = project_ID).project_directory
    project_json_name = "hyperparameter.json"
    if os.path.exists(os.path.join(project_path, project_json_name)):
        with open(os.path.join(project_path, project_json_name), 'r') as f:
            context = json.load(f)
            context['status'] = 200
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse({'status':204})

def trainSave(request, pk, pid):
    project_ID = pid
    user = User.objects.get(pk = pk)
    project = Project.objects.filter(project_id = project_ID, user_id= user)
    if project is None:
        return JsonResponse({"status": 500})
    project_path = Project.objects.only('project_directory').get(project_id = project_ID).project_directory
    project_json_name = "hyperparameter.json"
    project_json = request.POST.get("config")
    project_json = json.loads(project_json)
    with open(os.path.join(project_path, project_json_name), 'w') as f:
        json.dump(project_json, f)
    main(project_path= project_path, pid= str(project_ID))
    context = {"status":200}
    return JsonResponse(context, safe=False)

def trainRun(request, pk, pid):
    context = {"isRun": True}
    project_path = Project.objects.get(project_id = pid).project_directory
    cmd("python "+os.path.join(project_path, str(pk)+".py"))
    return JsonResponse(context, safe=False)

def trainEpoch(request, pk, pid):
    project_path = Project.objects.get(project_id = pid).project_directory
    with open(os.path.join(project_path,"epoch"), "r") as f:
        epoch = f.read()
    context = {"epoch:", epoch}
    return JsonResponse(context, safe=False)

def trainROC(request, pk, pid):
    project_path = Project.objects.get(project_id = pid).project_directory
    file_path = os.path.join(project_path, "auc.png")
    try:
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response["Content-type"] = "application/png"
    except Exception as e:
        return JsonResponse({'status':500})
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(project_ID)
    return response

def trainACC(request, pk, pid):
    project_path = Project.objects.get(project_id = pid).project_directory
    file_path = os.path.join(project_path, "acc.png")
    try:
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response["Content-type"] = "application/png"
    except Exception as e:
        return JsonResponse({'status':500})
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(pid)
    return response

# Front
# POST: 还不是很清楚
def uploadDataset(request, pk):
    file = request.FILES['file']
    if file is None:
        return JsonResponse({"status":400})
    name = file.name[:-5]
    file_path = os.path.join(settings.MEDIA_ROOT, str(pk), "data", name)
    save_path = os.path.join(settings.MEDIA_ROOT, str(pk), "data")

    user = User.objects.get(pk = pk)
    is_save = Data.objects.filter(user_id = user, dataset_name=name)
    data = Data.objects.create(user_id=user, dataset_name=name, dataset_directory= file_path)

    if data is None or is_save.count() != 0 :
        status = 400
    else:
        data.save()
        status = 200

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # save file
    file_path = os.path.join(save_path, data.dataset_name)
    with open(file_path, 'wb+') as fp:
        for chunk in file.chunks():
            fp.write(chunk)

    context = {"status": status}
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
    user = User.objects.get(pk = user_ID)
    userProject = Users_template(project_id=project_ID, user_id=user)
    userProject.save()
    context = {'isStar': True}
    return JsonResponse(context, safe=False)

