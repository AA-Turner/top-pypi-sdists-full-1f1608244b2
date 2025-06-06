# Generated by Django 5.0.14 on 2025-05-21 11:05

from django.conf import settings
from django.db import migrations, models
from django.db.models import Count


def handle_duplicates(apps, schema_editor):
    NotificationTypeSetting = apps.get_model("notifications", "NotificationTypeSetting")
    for row in NotificationTypeSetting.objects.values('user', 'notification_type').annotate(c=Count("*")).filter(c__gt=1):
        duplicates = NotificationTypeSetting.objects.filter(user=row['user'], notification_type=row['notification_type'])
        for duplicate in duplicates[1:]:
            duplicate.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_notificationtype_is_lock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(handle_duplicates),
        migrations.AlterModelOptions(
            name='notificationtypesetting',
            options={'verbose_name': 'Notification Type Setting', 'verbose_name_plural': 'Notification Type Settings'},
        ),
        migrations.AddConstraint(
            model_name='notificationtypesetting',
            constraint=models.UniqueConstraint(fields=('user', 'notification_type'), name='unique_notification_setting'),
        ),
    ]
