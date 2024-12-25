from django.urls import path, include

from .views import EmployeesAPIList

urlpatterns = [
    path('employees_list', EmployeesAPIList.as_view())
]