from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class StudentInformation(models.Model):
    """
    Stores additional information about each student.
    Connected with Django's default User model using OneToOne relation.
    """
    GENDER_CHOICES = [
        ("male", "مرد"),     # Male
        ("female", "زن"),    # Female
    ]

    YEAR_CHOICES = [
        ("one", "اول"),
        ("two", "دوم"),
        ("three", "سوم"),
        ("four", "چهارم"),
        ("five", "پنجم"),
        ("six", "شیشم"),
        ("seven", "هفتم"),
        ("eight", "هشتم"),
        ("nine", "نهم"),
        ("ten", "دهم"),
        ("eleven", "یازدهم"),
        ("twelve", "دوازدهم"),
        ("thirteen", "پشت کنکور"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_code = models.CharField(max_length=10, unique=True)  # Student ID code
    birthday = models.DateField()  # Date of birth
    year = models.CharField(max_length=15, choices=YEAR_CHOICES)  # School year
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # Gender

    def __str__(self):
        return f'User: {self.user.get_full_name()} - Year: {self.get_year_display()}'


class OtpCode(models.Model):
    """
    Stores OTP (One Time Password) for user verification.
    Each user can have only one OTP at a time.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # 6-digit code (supports leading zeros like 000123)
    created = models.DateTimeField(auto_now_add=True)  # Auto-set on creation

    def __str__(self):
        return f'User: {self.user.username}, Code: {self.code}, Created: {self.created}'

    def is_valid(self):
        """
        Returns True if OTP is still valid (within 2 minutes of creation).
        Otherwise returns False.
        """
        expire_time = self.created + timedelta(minutes=2)
        return datetime.now() <= expire_time


class Teacher(models.Model):
    """
    Stores information about teachers.
    """
    full_name = models.CharField(max_length=255)  # Teacher's full name
    about = models.TextField()  # Biography / description

    def __str__(self):
        return self.full_name
