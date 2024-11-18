from rest_framework.viewsets import ModelViewSet
from .models import User
from students.models import Student
from students.serializers import StudentSerializer
from users.permissions import IsAdmin, IsTeacher, IsStudent
from rest_framework import generics
from .serializers import UserSerializer
import logging

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action == 'list':  # Viewing all students
            return [IsTeacher() | IsAdmin()]
        elif self.action == 'retrieve':  # Viewing a single student
            return [IsStudent() | IsTeacher() | IsAdmin()]
        elif self.action in ['create', 'update', 'destroy']:  # Modifying data
            return [IsAdmin()]
        return super().get_permissions()

logger = logging.getLogger(__name__)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        logger.info(f'User registered: {user.username}')