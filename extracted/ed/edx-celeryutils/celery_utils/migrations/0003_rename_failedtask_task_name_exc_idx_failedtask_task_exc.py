# Generated by Django 4.2.11 on 2025-04-09 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celery_utils', '0002_chordable_django_backend'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='failedtask',
            new_name='idx_failedtask_task_exc',
            old_fields=('task_name', 'exc'),
        ),
    ]
