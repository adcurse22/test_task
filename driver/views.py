from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DriverLogSerializer
from .services import DriverTimeCalculator
from .models import DriverLog

class DriverWorkingTimeView(APIView):
    def get(self, request, driver_id, format=None):
        driver_logs = DriverLog.objects.filter(driver_id=driver_id)
        serializer = DriverLogSerializer(driver_logs, many=True)

        calculator = DriverTimeCalculator()
        daily_work_time = calculator.calculate_daily_working_time(driver_logs)

        response_data = {
            'driver_logs': serializer.data,
            'daily_work_time': daily_work_time.total_seconds() / 3600
        }
        return Response(response_data)
