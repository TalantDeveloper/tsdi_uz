from django.contrib import admin
from .models import Partner, Department, Employee, Rectory, Service, Sahifalar
from modeltranslation.admin import TranslationAdmin

@admin.register(Partner)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', "name", 'url', 'image')
    list_display_links = ('id', 'name', 'url', 'image')
    search_fields = ('id', 'name', 'url')

@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'sees', 'create_at')
    list_display_links = ('id', 'name', 'sees', 'create_at')
    search_fields = ('name', )
    # paginator = 20

@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'email', 'department', 'phone_number', 'is_chief')
    list_display_links = ('id', 'name', 'email', 'department', 'phone_number', 'is_chief')
    search_fields = ('name', 'department')
    filter = ('is_chief', )
    # paginator = 20


@admin.register(Rectory)
class RectoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'phone_number', 'is_rector', 'position')
    list_display_links = ('id', 'name', 'phone_number', 'is_rector', 'position')
    search_fields = ('name', 'position', 'phone_number')
    filter = ('is_rector',)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['name', 'icon_class', 'url']
    list_display_links = ['name', 'icon_class', 'url']
    search_fields = ['name', 'icon_class', 'url']

@admin.register(Sahifalar)
class SahifalarAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'page_name']
    list_display_links = ['id', 'title', 'page_name']
    search_fields = ['id', 'title', 'page_name']
