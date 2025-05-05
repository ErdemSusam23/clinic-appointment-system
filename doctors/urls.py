from django.urls import path
from .views import DepartmentListView, DepartmentDoctorsView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/doctors/', DepartmentDoctorsView.as_view(), name='department-doctors'),
]
