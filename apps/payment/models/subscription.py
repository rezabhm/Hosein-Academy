from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.package.models.package import Course


class PaymentType(models.TextChoices):
    """
    Enum-like class for payment type choices.
    """
    INSTALLMENT = 'installment', _("Installment")
    IMMEDIATE = 'immediate', _("Immediate")


class Subscription(BaseModel):
    """
    Represents a user's subscription to a course.
    Stores the user, course, and payment type information.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name=_("User"),
        help_text=_("The user who subscribed to the course.")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name=_("Course"),
        help_text=_("The course the user is subscribed to.")
    )
    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        default=PaymentType.INSTALLMENT,
        verbose_name=_("Payment Type"),
        help_text=_("Type of payment (installment or immediate).")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("Timestamp when the subscription was created.")
    )

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='unique_user_course_subscription'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class InstallmentPayment(BaseModel):
    """
    Represents an installment payment for a subscription.
    Stores the due date, price, and payment status.
    """
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        related_name='installment_payments',
        verbose_name=_("Subscription"),
        help_text=_("The subscription this installment payment belongs to.")
    )
    payment_due_date = models.DateField(
        verbose_name=_("Payment Due Date"),
        help_text=_("The due date for this installment payment.")
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"),
        help_text=_("The amount of this installment payment in the smallest currency unit.")
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name=_("Is Paid"),
        help_text=_("Indicates if the installment has been paid.")
    )

    class Meta:
        verbose_name = _("Installment Payment")
        verbose_name_plural = _("Installment Payments")
        ordering = ['payment_due_date']

    def __str__(self):
        return f"Installment for {self.subscription} due {self.payment_due_date}"


class ImmediatePayment(BaseModel):
    """
    Represents an immediate (one-time) payment for a subscription.
    Stores the price and links to the subscription.
    """
    subscription = models.OneToOneField(
        Subscription,
        on_delete=models.CASCADE,
        related_name='immediate_payment',
        verbose_name=_("Subscription"),
        help_text=_("The subscription this immediate payment belongs to.")
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"),
        help_text=_("The amount of the immediate payment in the smallest currency unit.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("Timestamp when the payment was created.")
    )

    class Meta:
        verbose_name = _("Immediate Payment")
        verbose_name_plural = _("Immediate Payments")
        ordering = ['-created_at']

    def __str__(self):
        return f"Immediate payment for {self.subscription}"