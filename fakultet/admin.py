from django.contrib import admin
from .models import Chair, TeacherChair, New, Faculty, TeacherFaculty
from modeltranslation.admin import TranslationAdmin


@admin.register(Chair)
class ChairAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'sub_name', 'content']
    list_display_links = ['id', 'name', 'sub_name', 'content']
    filter = ['name', 'sub_name']
    search_fields = ['id', 'name', 'sub_name']

@admin.register(TeacherChair)
class TeacherChairAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'chair', 'phone_num', 'email', 'position']
    list_display_link = ['id', 'name', 'chair', 'phone_num', 'email', 'position']
    search_fields = ['id', 'name', 'chair', 'phone_num']


@admin.register(New)
class NewAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'sees', 'create_at', 'update_at']
    list_display_link = ['id', 'title', 'sees', 'create_at', 'update_at']
    filter = ['chair']
    search_fields = ['id', 'title', 'chair']


@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'content']
    list_display_links = ['id', 'name', 'content']
    filter = ['kafedra']
    search_fields = ['id', 'name', 'kafedra']


@admin.register(TeacherFaculty)
class TeacherFacultyAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'fakultet', 'phone_number', 'position', 'is_dean']
    list_display_links = ['id', 'name', 'fakultet', 'phone_number', 'position', 'is_dean']
    filter = ['fakultet']
    search_fields = ['id', 'name', 'phone_number']