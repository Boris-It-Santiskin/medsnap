from django.shortcuts import render
from rest_framework import generics
from .serializer import AbstractClinicalEmployeeSerializer
from  .models import *

# Create your views here.

class EmployeesAPIList(generics.ListAPIView):
    queryset = AbstractClinicalEmployee.objects.all()
    print(queryset)
    serializer_class = AbstractClinicalEmployeeSerializer