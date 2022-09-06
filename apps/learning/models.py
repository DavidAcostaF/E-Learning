import uuid
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
    classroom_code = models.CharField(max_length=14)
    state = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=False,auto_now_add=True)
    visibility = models.IntegerField(choices=visibility,default=0)

    def __str__(self):
        return f'{self.name}'

class ClassPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    class_room = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    files = models.FileField(upload_to='files_posts',null=True,blank=True)

