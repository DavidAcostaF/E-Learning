from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from apps.learning.forms import FormClassRoom

from apps.learning.models import ClassRoom
# Create your views here.

class tem(TemplateView):
    template_name = 'base.html'


class CreateClasroom(CreateView):
    model = ClassRoom
    form_class = FormClassRoom
    success_url = reverse_lazy('index')
    template_name = 'classroom/create_classroom.html'

class JoinInClass(CreateView):
    model = ClassRoom

    def post(self,request):
        class_code = request.POST.get('class_code')
        if class_code:
            code = self.model.objects.get(classroom_code = class_code)
            user = request.user
            code.user.add(user)
            #code.save()
            return redirect('index')
            return redirect('index')


