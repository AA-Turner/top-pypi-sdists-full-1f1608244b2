# Generated by Django 4.1.8 on 2023-04-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agenda", "0003_calendaritem_endpoint_basename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendaritem",
            name="item_type",
            field=models.CharField(default="agenda.CalendarItem", max_length=255, verbose_name="Type"),
        ),
    ]
