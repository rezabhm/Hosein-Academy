from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.package.models.package import Course


class Category(models.Model):
    """
    Represents a category for organizing courses.
    Stores the category title and enables association with multiple courses.
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_("Category Title"),
        help_text=_("The title of the category (up to 255 characters).")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['title']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    """
    Represents a Frequently Asked Question (FAQ) related to a course.
    Stores the question, answer, and associated course.
    """
    question = models.TextField(
        verbose_name=_("Question"),
        help_text=_("The question text for the FAQ.")
    )
    answer = models.TextField(
        verbose_name=_("Answer"),
        help_text=_("The answer text for the FAQ.")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='faqs',
        verbose_name=_("Course"),
        help_text=_("The course this FAQ is associated with.")
    )

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ['course', 'question']

    def __str__(self):
        return f"FAQ: {self.question[:50]}"


class Comment(models.Model):
    """
    Represents a user comment on a course.
    Stores the comment text, associated user, and course.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='course_comments',
        verbose_name=_("User"),
        help_text=_("The user who posted the comment.")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("Course"),
        help_text=_("The course this comment is associated with.")
    )
    comment_text = models.TextField(
        verbose_name=_("Comment Text"),
        help_text=_("The content of the comment.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("Timestamp when the comment was created.")
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['course', '-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.course.title}"