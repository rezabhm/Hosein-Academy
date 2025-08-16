from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.payment.models.subscription import Subscription, InstallmentPayment, ImmediatePayment


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Subscription model.
    """
    list_display = ('user', 'course', 'payment_type', 'created_at')
    list_filter = ('payment_type', 'course', 'created_at')
    search_fields = ('user__username', 'course__title')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        (_("Subscription Details"), {
            'fields': ('user', 'course', 'payment_type'),
            'description': _("Manage subscription details.")
        }),
    )

    inlines = [
        # Defined below to avoid forward reference issues
    ]

    def get_readonly_fields(self, request, obj=None):
        """Make created_at readonly in the admin interface."""
        return ['created_at'] if obj else []


@admin.register(InstallmentPayment)
class InstallmentPaymentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the InstallmentPayment model.
    """
    list_display = ('subscription', 'payment_due_date', 'amount', 'is_paid')
    list_filter = ('is_paid', 'payment_due_date', 'subscription__course')
    search_fields = ('subscription__user__username', 'subscription__course__title')
    ordering = ('payment_due_date',)

    fieldsets = (
        (_("Installment Details"), {
            'fields': ('subscription', 'payment_due_date', 'amount', 'is_paid'),
            'description': _("Manage installment payment details.")
        }),
    )


@admin.register(ImmediatePayment)
class ImmediatePaymentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ImmediatePayment model.
    """
    list_display = ('subscription', 'amount', 'created_at')
    list_filter = ('created_at', 'subscription__course')
    search_fields = ('subscription__user__username', 'subscription__course__title')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        (_("Payment Details"), {
            'fields': ('subscription', 'amount'),
            'description': _("Manage immediate payment details.")
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Make created_at readonly in the admin interface."""
        return ['created_at'] if obj else []


class InstallmentPaymentInline(admin.TabularInline):
    """
    Inline admin for InstallmentPayments within a Subscription.
    """
    model = InstallmentPayment
    extra = 1
    fields = ('payment_due_date', 'amount', 'is_paid')
    ordering = ('payment_due_date',)


class ImmediatePaymentInline(admin.TabularInline):
    """
    Inline admin for ImmediatePayment within a Subscription.
    """
    model = ImmediatePayment
    extra = 0
    fields = ('amount', 'created_at')
    readonly_fields = ('created_at',)


# Register inlines with SubscriptionAdmin
SubscriptionAdmin.inlines = [InstallmentPaymentInline, ImmediatePaymentInline]