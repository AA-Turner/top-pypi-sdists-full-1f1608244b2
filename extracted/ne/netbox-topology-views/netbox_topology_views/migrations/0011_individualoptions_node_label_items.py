# Generated by Django 5.0.9 on 2024-09-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_topology_views', '0010_individualoptions_grid_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualoptions',
            name='node_label_items',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
