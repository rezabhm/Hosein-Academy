from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.package.models.package import Course, Season, Lesson
from apps.package.models.insights import Category, FAQ, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('title',),
            'description': _("Manage category details.")
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Course model.
    """
    list_display = ('title', 'current_price', 'discounted_price', 'has_installment_payment', 'total_hours')
    list_filter = ('has_installment_payment', 'categories')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories', 'teachers')
    ordering = ('title',)

    fieldsets = (
        (_("Basic Information"), {
            'fields': ('title', 'description', 'banner'),
            'description': _("Core details of the course.")
        }),
        (_("Pricing"), {
            'fields': ('current_price', 'discounted_price', 'has_installment_payment', 'installment_payment_count'),
            'description': _("Pricing and payment options.")
        }),
        (_("Relationships"), {
            'fields': ('categories', 'teachers', 'total_hours'),
            'description': _("Course categories, teachers, and duration.")
        }),
    )

    inlines = [
        # Defined below to avoid forward reference issues
    ]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Season model.
    """
    list_display = ('name', 'course')
    list_filter = ('course',)
    search_fields = ('name', 'course__title')
    ordering = ('course', 'name')

    fieldsets = (
        (None, {
            'fields': ('name', 'course'),
            'description': _("Manage season details.")
        }),
    )

    inlines = [
        # Defined below to avoid forward reference issues
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Lesson model.
    """
    list_display = ('title', 'season', 'duration_minutes', 'is_free')
    list_filter = ('is_free', 'season__course')
    search_fields = ('title', 'season__name', 'season__course__title')
    ordering = ('season', 'title')

    fieldsets = (
        (None, {
            'fields': ('title', 'video_url', 'duration_minutes', 'is_free', 'season'),
            'description': _("Manage lesson details.")
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FAQ model.
    """
    list_display = ('question_preview', 'course')
    list_filter = ('course',)
    search_fields = ('question', 'answer', 'course__title')
    ordering = ('course', 'question')

    def question_preview(self, obj):
        """Returns a truncated version of the question for display."""
        return obj.question[:50] + ('...' if len(obj.question) > 50 else '')
    question_preview.short_description = _("Question")

    fieldsets = (
        (None, {
            'fields': ('question', 'answer', 'course'),
            'description': _("Manage FAQ details.")
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    """
    list_display = ('user', 'course', 'comment_preview', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('comment_text', 'user__username', 'course__title')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def comment_preview(self, obj):
        """Returns a truncated version of the comment for display."""
        return obj.comment_text[:50] + ('...' if len(obj.comment_text) > 50 else '')
    comment_preview.short_description = _("Comment")

    fieldsets = (
        (None, {
            'fields': ('user', 'course', 'comment_text'),
            'description': _("Manage comment details.")
        }),
    )


class LessonInline(admin.TabularInline):
    """
    Inline admin for Lessons within a Season.
    """
    model = Lesson
    extra = 1
    fields = ('title', 'video_url', 'duration_minutes', 'is_free')
    ordering = ('title',)


class SeasonInline(admin.TabularInline):
    """
    Inline admin for Seasons within a Course.
    """
    model = Season
    extra = 1
    fields = ('name',)
    ordering = ('name',)


# Register inlines with their respective admins
CourseAdmin.inlines = [SeasonInline]
SeasonAdmin.inlines = [LessonInline]