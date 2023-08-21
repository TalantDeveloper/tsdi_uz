from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('gerb/', views.gerb, name='gerb'),
    path('bayroq/', views.bayroq, name='bayroq'),
    path('madhiya/', views.madhiya, name='madhiya'),
    path('vazifa/', views.vazifa, name='vazifa'),
    path('rektorat/', views.rektorat, name='rektorat'),
    path('qabulxona/', views.qabul, name='qabulxona'),
    # path('qabulxona/xabar', views.store, name='xabar'),           shu yer chala
    path('i-xizmatlar/', views.xizmatlar, name='xizmatlar'),
    path('sahifa/<str:page>/', views.sahifalar, name='sahifa'),
    path('markazlar/', views.markazlar, name='markazlar'),
    path('markaz/<int:pk>/', views.markaz, name='markaz'),
    path('yangiliklar/', views.yangiliklar, name='yangiliklar'),
    path('yangilik/<int:pk>/', views.yangilik, name='yangilik'),
    path('antikorrupsiya/', views.antikorrupsiya, name='antikorrupsiya'),

]
