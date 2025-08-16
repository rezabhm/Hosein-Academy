from django.contrib import admin
from .models import StudentInformation, OtpCode, Teacher


@admin.register(StudentInformation)
class StudentInformationAdmin(admin.ModelAdmin):
    list_display = ("user", "id_code", "year", "gender")  # Fields displayed in list view
    search_fields = ("user__username", "id_code")         # Searchable fields in admin
    list_filter = ("year", "gender")                      # Filters in the right sidebar


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "create_at")   # Fields displayed in list view
    search_fields = ("user__username", "code")   # Searchable fields in admin


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("full_name",)   # Fields displayed in list view
    search_fields = ("full_name",)  # Searchable fields in admin
