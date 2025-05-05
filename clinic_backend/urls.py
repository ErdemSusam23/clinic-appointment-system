from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Schema view configuration
schema_view = get_schema_view(
   openapi.Info(
      title="Clinic Appointment System API",
      default_version='v1',
      description="API documentation for Clinic Appointment System",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   url=settings.NGROK_URL if hasattr(settings, 'NGROK_URL') else None,  # Dynamic URL for ngrok
)

urlpatterns = [
    # Root URL redirects to API documentation
    path('', RedirectView.as_view(url='/api/docs/swagger/', permanent=False)),
    
    # Django Admin
    path('admin/', admin.site.urls),
    
    # Your API endpoints
    path('api/', include('appointments.urls')),
    path('api/', include('users.urls')),
    
    # Documentation URLs (works with both localhost and ngrok)
    re_path(r'^api/docs/swagger(?P<format>\.json|\.yaml)$', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'),
    re_path(r'^api/docs/swagger/$', 
            schema_view.with_ui('swagger', cache_timeout=0), 
            name='schema-swagger-ui'),
    re_path(r'^api/docs/redoc/$', 
            schema_view.with_ui('redoc', cache_timeout=0), 
            name='schema-redoc'),
]

# Add this if you're serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)