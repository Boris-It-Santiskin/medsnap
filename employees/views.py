from django.shortcuts import render
from rest_framework import generics
from  .models import *

# Create your views here.

class EmployeesAPIList(generics.ListAPIView):
    employees_list = AbstractClinicalEmployee.objects.all()
    serializer_class =