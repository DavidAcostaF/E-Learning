from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from apps.learning.forms import FormClassRoom,FormPost

from apps.learning.models import ClassPosts, ClassRoom
# Create your views here.

# class tem(TemplateView):
#     template_name = 'base.html'

class MyClass(ListView):
    model = ClassRoom
    template_name = 'classroom/home.html'

    def get_queryset(self):
        user = self.request.user
        context = self.model.objects.filter(user = user)
        return context


class CreateClasroom(CreateView):
    model = ClassRoom
    form_class = FormClassRoom
    success_url = reverse_lazy('home')
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


class DetailClassroom(DetailView):
    model = ClassRoom
    form_class = FormPost
    template_name = 'classroom/detail_classroom.html'

    def get_object(self,**kwargs):
        return self.model.objects.get(classroom_code = self.kwargs['classroom_code'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['posts'] = ClassPosts.objects.filter(class_room__classroom_code = self.kwargs['classroom_code'])
        return context


class CreatePosts(CreateView):
    model = ClassPosts
    form_class = FormPost
    def post(self,request,slug):
        form = self.form_class(request.POST,request.FILES)
        print(slug)
        room = ClassRoom.objects.get(classroom_code = slug)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            file_name = request.POST.get('file_name')
            files = request.FILES.get('file')
            self_post = self.model.objects.create(title = title,content = content,class_room=room,user = user,files = files)
            if file_name:
                self_post.files_name = file_name
                self_post.save()
        else:
            print(form.errors)
        return redirect(request.META.get('HTTP_REFERER'))

class DetailActivity(DetailView):
    model = ClassPosts
    template_name = 'classroom/detail_activity.html'
    context_object_name = 'activity'

