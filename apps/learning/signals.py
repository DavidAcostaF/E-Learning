import uuid
from django.db.models.signals import post_save

from .models import ClassRoom


def ClassCode(sender,instance,**kwargs):
    if not instance.classroom_code:
        print(instance.classroom_code)
        uid = str(uuid.uuid4())[:13]
        instance.classroom_code = uid
        instance.save()
        
post_save.connect(ClassCode,sender = ClassRoom)