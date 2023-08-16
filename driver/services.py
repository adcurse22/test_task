
from datetime import timedelta


class DriverTimeCalculator:
    def calculate_daily_working_time(self, driver_logs):
        total_work_time = timedelta()

        for i in range(len(driver_logs) - 1):
            current_log = driver_logs[i]
            next_log = driver_logs[i + 1]

            if current_log.status == 'WORK':
                total_work_time += next_log.create_date - current_log.create_date

        return total_work_time
