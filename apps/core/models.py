from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.text import slugify
from django.utils import timezone


class BaseModel(models.Model):

    slug = models.SlugField(unique=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def save(
        self,
        *args,
        **kwargs,
    ):

        self.update_at = timezone.now()

        if self.create_at is None:
            self.create_at = timezone.now()

        if self.slug is None:
            self.slug = slugify(f'{self.create_at}+{self.update_at}')

        super().save(*args, **kwargs)


class StudentInformation(BaseModel):
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


class OtpCode(BaseModel):
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


class Teacher(BaseModel):
    """
    Stores information about teachers.
    """
    full_name = models.CharField(max_length=255)  # Teacher's full name
    about = models.TextField()  # Biography / description

    def __str__(self):
        return self.full_name
