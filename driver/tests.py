from django.test import TestCase
from .models import DriverLog
from .services import DriverTimeCalculator
from django.utils import timezone


class DriverWorkingTimeTest(TestCase):
    def setUp(self):
        self.driver_log1 = DriverLog.objects.create(
            company_id=1,
            driver_id=1,
            create_date=timezone.now(),
            status='WORK'
        )
        self.driver_log2 = DriverLog.objects.create(
            company_id=1,
            driver_id=1,
            create_date=timezone.now(),
            status='REST'
        )

    def test_daily_working_time(self):
        # Создаем две записи с разными статусами и временными метками
        now = timezone.now()
        self.driver_log1 = DriverLog.objects.create(
            company_id=1,
            driver_id=1,
            create_date=now,
            status='WORK'
        )
        self.driver_log2 = DriverLog.objects.create(
            company_id=1,
            driver_id=1,
            create_date=now + timezone.timedelta(hours=1.5),  # Добавляем час к времени
            status='REST'
        )

        driver_logs = [self.driver_log1, self.driver_log2]
        calculator = DriverTimeCalculator()
        daily_work_time = calculator.calculate_daily_working_time(driver_logs)

        expected_daily_work_hours = 1.5

        self.assertEqual(daily_work_time.total_seconds() / 3600, expected_daily_work_hours)

