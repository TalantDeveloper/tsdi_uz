from django.urls import path
from . import views

app_name = 'faculty'
urlpatterns = [
    path('fakultetlar/', views.faculties_view, name='fakultetlar'),
    path('fakultet/<str:sub_name>/', views.faculty_view, name='fakultet'),
    path('kafedralar/', views.kafedralar_view, name='kafedralar'),
    path('kafedra/<str:sub_name>/', views.kafedra_view, name='kafedra'),
]
