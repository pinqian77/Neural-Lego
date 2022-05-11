from django.test import TestCase,Client
from django.contrib.auth.models import User
from lego.models import Comment, Data, Project, Users_data, Users_project, Users_template
import json

class TestViews(TestCase):
    #login
    def test_login_Post(self):
        response = Client().post('login/',{'username':'Bob','password':'Bob12345#'})
        self.assertEquals(response['status'], 200)
        self.assertEquals(response['uid'],2)
    #username和passwprd任意一个为空都可，代码只展现一种情况
    def test_login_nodata_Post(self):
        response = Client().post('login/', {'username': '', 'password': 'Bob12345#'})
        self.assertEquals(response['status'], 404)

    def test_login_wrongpassword_Post(self):
        response = Client().post('login/', {'username': 'Bob', 'password': 'Bob123456#'})
        self.assertEquals(response['status'], 404)

    #register
    def test_register_Post(self):
        response = Client().post('register/', {'username': 'Jerry', 'password': 'Jerry12345#'})
        self.assertEquals(response['status'], 200)

    def test_register_samename_Post(self):
        response = Client().post('register/', {'username': 'Bob', 'password': 'Bob12345#'})
        self.assertEquals(response['status'], 500)

    # username和passwprd任意一个为空都可，代码只展现一种情况
    def test_register_nodata_Post(self):
        response = Client().post('register/', {'username': '', 'password': 'Bob12345#'})
        self.assertEquals(response['status'], 500)
    #不符合条件的密码
    def test_register_wrongpassword_Post(self):
        response = Client().post('register/', {'username': 'Jerry', 'password': 'Jerry'})
        self.assertEquals(response['status'], 404)

    #projectPage
    #访客模式的默认用户
    def test_guest_GET(self):
        response = Client().get('project/1/')
        self.assertEquals(response['status'],200)
        self.assertEquals(response['project_detail']['project_id'], 1)
    #用户
    def test_user_GET(self):
        response = Client().get('project/2/')
        self.assertEquals(response['status'],200)
        self.assertEquals(response['project_detail']['project_id'], 2)

    #datapage
    # 访客模式的默认用户
    def test_guest_GET(self):
        response = Client().get('dataset/1/')
        self.assertEquals(response['status'], 200)
        self.assertEquals(response['project_detail']['data_id'], 1)

    # 用户
    def test_user_GET(self):
        response = Client().get('dataset/2/')
        self.assertEquals(response['status'], 200)
        self.assertEquals(response['project_detail']['data_id'], 1)


    #deleteData
    def test_deletedata_GET(self):
        response = Client().get('dataset/remove/2/1/')
        self.assertEquals(response['status'], 200)
    #data空
    def test_nodata_GET(self):
        response = Client().get('dataset/remove/2/2/')
        self.assertEquals(response['status'], 500)


    #deleteProject
    def test_deleteproject_GET(self):
        response = Client().get('project/remove/2/1/')
        self.assertEquals(response['status'], 200)
    #project空
    def test_noproject_GET(self):
        response = Client().get('project/remove/2/2/')
        self.assertEquals(response['status'], 500)

#search
    def test_search_Post(self):
        response = Client().post('project/search/2/', {'keyword': 'Project'})
        self.assertEquals(response['status'], 200)
        self.assertEquals(response['project_detail']['project_id'], 2)

    #newProject
    def test_newProject_Post(self):
        response = Client().post('project/create/2/', {"name": 'Project3',"is_public":'True'})
        self.assertEquals(response['status'], 200)

     #空的project name 和 is_public
    def test_newProject_Post(self):
        response = Client().post('project/create/2/', {"name": '', "is_public": ''})
        self.assertEquals(response['status'], 400)

    #trainSave
    def test_trainSave_GET(self):
        response = Client().get('train/apply/2/2/')
        self.assertEquals(response['status'], 200)
    #没有项目
    def test_trainSave_GET(self):
        response = Client().get('train/apply/2/3/')
        self.assertEquals(response['status'], 500)

    #trainRun
    def test_trainRun_GET(self):
        response = Client().get('train/run/2/2/')
        self.assertEquals(response['status'], 200)
