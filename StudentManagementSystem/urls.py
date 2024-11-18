from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/students/', include('students.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Student Management API",
      default_version='v1',
      description="API documentation for Student Management System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@studentmanagement.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]