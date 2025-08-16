from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Transaction(BaseModel):
    """
    Represents a financial transaction made by a user.
    Stores the transaction amount, description, and associated user.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name=_("User"),
        help_text=_("The user who initiated the transaction.")
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"),
        help_text=_("The transaction amount in the smallest currency unit.")
    )
    description = models.CharField(
        max_length=255,
        verbose_name=_("Description"),
        help_text=_("A brief description of the transaction (up to 255 characters).")
    )

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        # ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.description} ({self.amount})"