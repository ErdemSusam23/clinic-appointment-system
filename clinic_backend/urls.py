from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Add this to include your appointments app API
    path('api/', include('appointments.urls')),  
]
