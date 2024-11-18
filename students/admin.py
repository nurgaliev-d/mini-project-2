from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'registration_date')
    search_fields = ('user__username', 'user__email')

admin.site.register(Student, StudentAdmin)