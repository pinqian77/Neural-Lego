from django.db import models

# Create your models here.

class Users_account(models.Model):
    user_id = models.AutoField(primary_key=True);
    accout_name = models.CharField(max_length=50, null=False)
    accout_password = models.CharField(max_length=50, null=False)
    last_login_time = models.DateField(null=False)
    def __str__(self):
        return self.user_id

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, null=False)
    project_directory = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=100, null=False)
    last_save_time = models.DateTimeField(null = False)
    is_public = models.CharField(max_length = 50, null=False)
    def __str__(self):
        return self.project_id

class Users_project(models.Model):
    F_user = models.ForeignKey(Users_account, on_delete=models.CASCADE)

    F_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    user_id = models.IntegerField(null=False);
    project_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id

class Users_template(models.Model):
    F_user = models.ForeignKey(Users_account, on_delete=models.CASCADE)

    F_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    user_id = models.IntegerField(null=False);
    project_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id

class Comment(models.Model):
    F_user = models.ForeignKey(Users_account, on_delete=models.CASCADE)

    F_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    comment_id = models.AutoField(primary_key=True)
    user_owner = models.IntegerField(null=False);
    user_target = models.IntegerField();
    project_id = models.IntegerField(null=False);
    content = models.CharField(max_length = 70, null=False);
    create_time = models.DateTimeField(null=False);
    like_count = models.IntegerField(default=0)
    def __str__(self):
        return self.comment_id

class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=50, null=False)
    data_directory = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=100, null=False)
    upload_time = models.DateTimeField(null = False)
    def __str__(self):
        return self.data_id

class User_data(models.Model):
    F_user = models.ForeignKey(Users_account, on_delete=models.CASCADE)

    F_data = models.ForeignKey(Data, on_delete=models.CASCADE, null=False)
    user_id = models.IntegerField(null=False);
    data_id = models.IntegerField(null=False);
    def __str__(self):
        return self.user_id
