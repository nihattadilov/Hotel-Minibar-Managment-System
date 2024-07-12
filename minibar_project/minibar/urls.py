from django.urls import path
from .views import index, room_sales, download_sales_report

urlpatterns = [
    path('', index, name='index'),
    path('room/<int:room_id>/sales/', room_sales, name='room_sales'),
    path('download_sales_report/', download_sales_report, name='download_sales_report'),
]
