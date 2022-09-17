import os
from django.db import models

from apps.users.models import MyUser

# Create your models here.
visibility = [
    (0,'Visible'),
    (1,'Ocult'),
    ]
class ClassRoom(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.CharField(max_length=150)
    user = models.ManyToManyField(MyUser)
    code = models.CharField(max_length=14)
    state = models.BooleanField(default=True)
    created_by = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='created_by')
    created_at = models.DateField(auto_now=False,auto_now_add=True)
    visibility = models.IntegerField(choices=visibility,default=0)

    def __str__(self):
        return f'{self.name}'

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    class_room = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    activity = models.CharField(max_length=50)
    files = models.FileField(upload_to='files_posts',null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def delete(self, *args, **kwargs):
        if self.files:
            self.files.delete()
        super().delete(*args, **kwargs)

class Files(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    activity = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='room')
    files = models.FileField(upload_to='UploadFiles',null=True,blank=True)
    comment = models.TextField(blank=True,null=True)
    upload_date = models.DateField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.files:
            self.files.delete()
        super().delete(*args, **kwargs)