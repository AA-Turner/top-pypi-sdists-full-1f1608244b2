# Generated by Django 5.0.13 on 2025-03-10 14:40

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0011_person_description_person_i18n'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
