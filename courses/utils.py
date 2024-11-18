from django.core.cache import cache
from courses.models import *

def get_cached_courses():
    courses = cache.get('courses')
    if not courses:
        courses = Course.objects.all()
        cache.set('courses', courses, timeout=3600)
    return courses
