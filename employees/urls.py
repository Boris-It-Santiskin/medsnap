from django.urls import path, include
from rest_framework.urls import app_name

app_name = 'employees'

urlpatterns = [
    path('', include('.snap/employees/urls'))
]