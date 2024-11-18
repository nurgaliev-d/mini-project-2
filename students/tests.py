from unittest import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

from users.models import User
from .models import Student

class StudentAPITest(TestCase):
       def setUp(self):
           self.client = APIClient()
           self.user = User.objects.create_user(username='testuser', password='testpass', role='student')
           self.client.login(username='testuser', password='testpass')
           self.student = Student.objects.create(user=self.user, dob='2000-01-01')

def test_student_list(self):
           response = self.client.get(reverse('student-list'))
           self.assertEqual(response.status_code, status.HTTP_200_OK)
           self.assertEqual(len(response.data), 1)

def test_student_detail(self):
           response = self.client.get(reverse('student-detail', args=[self.student.id]))
           self.assertEqual(response.status_code, status.HTTP_200_OK)
           self.assertEqual(response.data['user'], self.user.id)