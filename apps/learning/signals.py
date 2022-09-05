from .models import ClassRoom
from django.db.models.signals import post_save
import uuid

def ClassCode(sender,instance,**kwargs):
    class_code = instance
    if not class_code.classroom_code:
        uid = str(uuid.uuid4())[:10]
        class_code.uuid = uid
        class_code.save()
        
post_save.connect(ClassCode,sender = ClassRoom)