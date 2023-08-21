from .models import Chair, New, TeacherChair, Faculty, TeacherFaculty
from modeltranslation.translator import TranslationOptions, register


@register(Chair)
class ChairTranslationOption(TranslationOptions):
    fields = ('name', 'content')


@register(New)
class NewTranslationOption(TranslationOptions):
    fields = ('title', 'content')


@register(TeacherChair)
class TeacherChairTranslationOption(TranslationOptions):
    fields = ('position', 'academic_title')


@register(Faculty)
class FacultyTranslationOption(TranslationOptions):
    fields = ('name', 'content')


@register(TeacherFaculty)
class TeacherFacultyTranslationOption(TranslationOptions):
    fields = ('academic_title', 'position', 'reception_time')
