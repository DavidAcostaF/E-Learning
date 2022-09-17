from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView
from apps.learning.forms import FormClassRoom,FormPost,FormSubmitFiles
from django.db.models import Q
from apps.learning.models import Posts, ClassRoom,Files

# Create your views here.

# class tem(TemplateView):
#     template_name = 'base.html'

class MyClass(ListView):
    model = ClassRoom
    template_name = 'classroom/home.html'

    def get_queryset(self):
        user = self.request.user
        context = self.model.objects.filter(Q(user = user) | Q(created_by = user))
        print(context)
        return context


class CreateClasroom(CreateView):
    model = ClassRoom
    form_class = FormClassRoom
    success_url = reverse_lazy('home')
    template_name = 'classroom/create_classroom.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            user = request.user
            description = form.cleaned_data.get('description')
            self.model.objects.create(name = name,description=description,created_by = user)
        return redirect('create_classroom') 

class JoinInClass(CreateView):
    model = ClassRoom

    def post(self,request):
        class_code = request.POST.get('class_code')
        if class_code:
            code = self.model.objects.get(classroom_code = class_code)
            user = request.user
            code.user.add(user)
            #code.save()
            return redirect('create_classroom')
            return redirect('index')


class DetailClassroom(DetailView):
    model = ClassRoom
    form_class = FormPost
    template_name = 'classroom/detail_classroom.html'

    def get_object(self,**kwargs):
        return self.model.objects.get(code = self.kwargs['classroom_code'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['posts'] = Posts.objects.filter(class_room__code = self.kwargs['classroom_code'])
        return context


class CreateActivity(CreateView):
    model = Posts
    form_class = FormPost
    def post(self,request,slug):
        form = self.form_class(request.POST,request.FILES, form_kwargs=self.get_form_kwargs())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(request.META.get('HTTP_REFERER'))

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        query = ClassRoom.objects.get(code = slug)
        return query

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = self.request.user
        form_kwargs['code'] = self.get_queryset()
        print(self.get_queryset(),"123123")
        return form_kwargs

class DetailActivity(DetailView):
    model = Posts
    template_name = 'classroom/activity_detail.html'
    # context_object_name = 'activity'
    
    def get_context_data(self, **kwargs):
        activity = self.model.objects.get(pk = self.kwargs['pk'])
        user = self.request.user
        files = Files.objects.filter(user = user,activity = activity).first()
        context = {
            'files':files,
            'activity':activity
        }
        return context

class DeleteActivity(DeleteView):
    model = Posts

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        code = self.model.objects.get(id = pk)
        return reverse('detail_classroom', kwargs={'classroom_code': code.class_room.code})

class SubmitActivity(CreateView):
    model = Files
    form_class = FormSubmitFiles

    def post(self,request,pk):
        user = request.user
        file = request.FILES.get('file')
        activity = Posts.objects.get(id= pk)
        submit,created = self.model.objects.get_or_create(user = user,activity = activity)
        # if created:
        #     print('si')
        # else:
        submit.files = file
        submit.save()
        return redirect(request.META.get('HTTP_REFERER'))
        # created.save()


class CancelSubmit(CreateView):
    model = Files
    def post(self,request):
        