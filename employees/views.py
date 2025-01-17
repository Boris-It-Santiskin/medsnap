from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework import generics
from django.http import HttpResponse, JsonResponse

from .serializer import AbstractClinicalEmployeeSerializer
from  .models import *

from .forms import *



from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeesAPIList(generics.ListAPIView):
    queryset = AbstractClinicalEmployee.objects.all()
    print(queryset)
    serializer_class = AbstractClinicalEmployeeSerializer

from django.views.generic.edit import CreateView

from .forms import RegisterForm

class LoginView(View):  # Use a distinct name for the view
    def get(self, request):
        form = LoginForm()  # Instantiate the form
        context = {
            'title': 'login',
            'form': form,
            'button_submit':'Login'
        }
        return render(request, 'employeers_form_template.html', context)  # Pass the request object

    def post(self, request):
        form = LoginForm(data=request.POST)
        print('request.POST', request.method)
        if form.is_valid():
            cd = form.cleaned_data
            print('****',cd)
            email = cd['username']
            psw = cd['password']
            employee = authenticate(request,email=email, password=psw)
            print('-*-*-Employee', employee)
            if employee:
                login(request, employee)
            return redirect('main:index')  # Replace with your success URL

        return render(request, 'employeers_form_template.html', {'form': form, 'title': 'Login', 'button_submit': 'Login'})


class LogoutView(View):
    def get(self, request):
        # Log out the user
        logout(request)
        # Redirect to the login page or any other page
        return redirect('main:index')  # Replace 'login' with the name of your login URL pattern


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("<app_name>:<view_name>")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
