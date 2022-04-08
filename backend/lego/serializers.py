from rest_framework import serializers
from lego.models import Comment, Data, Project, Users_data, Users_project, Users_template
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'last_login']
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
#        fields = ['data_id', 'data_name', 'project_directory', 'discription', 'upload_time']
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
#        fields = ['comment_id', 'user_owner', 'user_target', 'project_id', 'content', 'create_time', 'like_count']
        fields = '__all__'
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_data
        fields = '__all__'
class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_project
        fields = '__all__'
class UserTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_template
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
       # fields = ['project_id', 'project_name', 'project_directory', 'discription', 'last_save_time', 'is_public']
        fields = '__all__'
