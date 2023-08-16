from django.db import models

class DriverLog(models.Model):
    company_id = models.IntegerField()
    driver_id = models.IntegerField()
    create_date = models.DateTimeField()
    status = models.CharField(max_length=20)  # Может быть 'WORK', 'REST', 'OFF', и т.д.
