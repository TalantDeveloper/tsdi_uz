from .models import Partner, Department, Employee, Rectory, Service, Sahifalar
from modeltranslation.translator import TranslationOptions,register


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('reception_time', 'position')

@register(Rectory)
class RectoryTranslationOptions(TranslationOptions):
    fields = ('content', 'academic_title', 'address', 'position', 'reception_time')

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ['name']

@register(Sahifalar)
class SahifalarTranslationOptions(TranslationOptions):
    fields = ['title', 'content']

