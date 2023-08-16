# Generated by Django 4.2.4 on 2023-08-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('driver_id', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
