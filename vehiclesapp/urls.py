from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_vehiculos, name='list'),
    path('create/', views.create_vehiculo, name='create'),
    path('update/<int:id>/', views.update_vehiculo, name='update'),
    path('delete/<int:id>/', views.delete_vehiculo, name='delete'),
]
