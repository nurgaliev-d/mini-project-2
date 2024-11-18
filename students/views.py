from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStudent

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Student.objects.all()
       serializer_class = StudentSerializer
       permission_classes = [IsAuthenticated, IsStudent]  # Only the student can access their record