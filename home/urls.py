from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('list-job/', home, name="job_list"),
   path('add_job/', add_job2, name="add_job"),
   path('', index, name="index"),
   path('index', index, name="index"),
]
