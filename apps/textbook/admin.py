from django.contrib import admin
from .models import TextBook
from django.utils.translation import gettext_lazy as _

@admin.register(TextBook)
class TextBookAdmin(admin.ModelAdmin):
    list_display = ("title", "pdf_file")  # Fields displayed in list view
    search_fields = ("title", "body")     # Searchable fields in admin
    help_text=_("Teachers associated with this course.")
    