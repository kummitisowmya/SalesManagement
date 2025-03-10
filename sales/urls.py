from django.urls import path
from .views import admin_dashboard, sales_dashboard

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('sales_dashboard/', sales_dashboard, name='sales_dashboard'),
]