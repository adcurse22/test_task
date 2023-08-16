
from django.urls import path
from .views import DriverWorkingTimeView

urlpatterns = [
    path('driver-working-time/<int:driver_id>/', DriverWorkingTimeView.as_view(), name='driver-working-time'),
    # Добавьте другие URL маршруты
]
