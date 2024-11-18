from django.urls import path
from .views import UserRegistrationView, StudentViewSet

urlpatterns = [
       path('register/', UserRegistrationView.as_view(), name='register'),
   ]