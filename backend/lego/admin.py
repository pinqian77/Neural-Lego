from django.contrib import admin

from .models import Comment, Data, Project 
from .models import Users_data, Users_project, Users_template
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Data)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Users_data)
admin.site.register(Users_project)
admin.site.register(Users_template)
