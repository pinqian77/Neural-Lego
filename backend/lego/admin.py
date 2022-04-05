from django.contrib import admin

from .models import Comment, Data, Project 
from .models import User_data, Users_account, Users_project, Users_template

# Register your models here.

admin.site.register(Data)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(User_data)
admin.site.register(Users_account)
admin.site.register(Users_project)
admin.site.register(Users_template)
