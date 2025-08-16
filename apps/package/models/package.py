from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import Teacher


class Course(models.Model):
    """
    Represents a course in the educational platform.
    Stores course metadata, pricing, and relationships with categories and teachers.
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_("Course Title"),
        help_text=_("The title of the course (up to 255 characters).")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Detailed description of the course content.")
    )
    banner = models.ImageField(
        upload_to='courses/banners/',
        verbose_name=_("Banner Image"),
        help_text=_("Banner image for the course.")
    )
    has_installment_payment = models.BooleanField(
        default=True,
        verbose_name=_("Supports Installment Payment"),
        help_text=_("Indicates if installment payment is available.")
    )
    installment_payment_count = models.PositiveIntegerField(
        default=3,
        verbose_name=_("Number of Installments"),
        help_text=_("Number of installment payments available.")
    )
    current_price = models.PositiveIntegerField(
        default=100_000_000,
        verbose_name=_("Current Price"),
        help_text=_("Current price of the course in the smallest currency unit.")
    )
    discounted_price = models.PositiveIntegerField(
        default=10_000_000,
        verbose_name=_("Discounted Price"),
        help_text=_("Discounted price of the course in the smallest currency unit.")
    )
    categories = models.ManyToManyField(
        'package.Category',
        related_name='courses',
        verbose_name=_("Categories"),
        help_text=_("Categories associated with this course.")
    )
    total_hours = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Total Hours"),
        help_text=_("Total duration of the course in hours.")
    )
    teachers = models.ManyToManyField(
        Teacher,
        related_name='courses',
        verbose_name=_("Teachers"),
        help_text=_("Teachers assigned to this course.")
    )

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ['title']

    def __str__(self):
        return self.title


class Season(models.Model):
    """
    Represents a season within a course.
    A season is a collection of lessons under a specific course.
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_("Season Name"),
        help_text=_("Name of the season (up to 100 characters).")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='seasons',
        verbose_name=_("Course"),
        help_text=_("The course this season belongs to.")
    )

    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")
        ordering = ['course', 'name']

    def __str__(self):
        return f"{self.course.title} - {self.name}"


class Lesson(models.Model):
    """
    Represents a single lesson within a season.
    Stores lesson metadata including video link and duration.
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_("Lesson Title"),
        help_text=_("Title of the lesson (up to 255 characters).")
    )
    video_url = models.URLField(
        verbose_name=_("Video URL"),
        help_text=_("URL to the lesson's video content.")
    )
    duration_minutes = models.PositiveIntegerField(
        verbose_name=_("Duration (Minutes)"),
        help_text=_("Duration of the lesson in minutes.")
    )
    is_free = models.BooleanField(
        default=False,
        verbose_name=_("Is Free"),
        help_text=_("Indicates if the lesson is free to access.")
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name=_("Season"),
        help_text=_("The season this lesson belongs to.")
    )

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ['season', 'title']

    def __str__(self):
        return f"{self.season} - {self.title}"
