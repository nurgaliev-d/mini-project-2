from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_grade_update_notification(student_email, grade):
    send_mail(
        'Grade Update',
        f'Your grade has been updated to: {grade}',
        'from@example.com',
        [student_email],
        fail_silently=False,
    )

@shared_task
def send_attendance_reminder(student_email):
    send_mail(
        'Attendance Reminder',
        'Please remember to mark your attendance today.',
        'from@example.com',
        [student_email],
        fail_silently=False,
    )