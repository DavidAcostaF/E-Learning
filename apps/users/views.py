from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
# Create your views here.
from .forms import FormUser

class Register(CreateView):
    template_name = 'users/register.html'
    form_class = FormUser

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password = password)
            login(request,user = user)
            return redirect('index')
        return redirect('register') 