from django.contrib import admin

from apps.learning.models import ClassRoom,Posts,Files

# Register your models here.

admin.site.register(ClassRoom)
admin.site.register(Posts)
admin.site.register(Files)