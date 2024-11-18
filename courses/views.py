from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated

from django.core.cache import cache

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cache_key = 'course_list'
        courses = cache.get(cache_key)
        if not courses:
            courses = list(Course.objects.all())
            cache.set(cache_key, courses, timeout=60*15) 
        return courses

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]