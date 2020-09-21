'''
URLs only for API views
'''
from django.urls import re_path, path, include
from rest_framework import routers

from .views import BranchListAPIView, EmployeeListAPIView

urlpatterns = (
    path('branch', BranchListAPIView.as_view()),
    re_path(r'employee.*', EmployeeListAPIView.as_view()),
)
