from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, null=False)
    project_directory = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=100, null=False)
    last_save_time = models.DateTimeField(auto_now_add=True)
    is_public = models.CharField(max_length = 50, null=False)
    star = models.IntegerField(null=False)
    def __str__(self):
        return str(self.project_id)
    class Meta:
        db_table = 'project'
        ordering = ['project_id']

class Users_project(models.Model):
    uppk = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False);
    project_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id
    class Meta:
        db_table = 'users_project'
        ordering = ['uppk']

class Users_template(models.Model):
    utpk = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False);
    project_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id
    class Meta:
        db_table = 'users_template'
        ordering = ['utpk']

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_owner = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    user_target = models.ForeignKey('User', on_delete=models.CASCADE)
    project_id = models.IntegerField(null=False);
    content = models.CharField(max_length = 70, null=False);
    create_time = models.DateTimeField(auto_now_add=True);
    like_count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.comment_id)
    class Meta:
        db_table = 'comment'
        ordering = ['comment_id']

class Data(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=50, null=False)
    data_directory = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=100, null=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.data_id)
    class Meta:
        db_table = 'data'
        ordering = ['data_id']

class Users_data(models.Model):
    udpk = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False);
    data_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id
    class Meta:
        db_table = 'users_data'
        ordering = ['udpk']

