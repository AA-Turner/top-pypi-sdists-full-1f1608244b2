# Generated by Django 5.0.8 on 2024-09-10 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="GroupObjectPermission",
                    fields=[
                        ("object_pk", models.CharField(max_length=255, verbose_name="object ID")),
                        ("id", models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                        ("editable", models.BooleanField(default=True)),
                        (
                            "content_type",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE, to="contenttypes.contenttype"
                            ),
                        ),
                        ("group", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.group")),
                        (
                            "permission",
                            models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.permission"),
                        ),
                    ],
                    options={
                        "db_table": "bridger_biggroupobjectpermission",
                        "abstract": False,
                        "default_related_name": "groupobjectpermissions",
                        "unique_together": {("group", "permission", "object_pk")},
                    },
                ),
                migrations.CreateModel(
                    name="UserObjectPermission",
                    fields=[
                        ("object_pk", models.CharField(max_length=255, verbose_name="object ID")),
                        ("id", models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                        ("editable", models.BooleanField(default=True)),
                        ("system", models.BooleanField(default=False)),
                        (
                            "content_type",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE, to="contenttypes.contenttype"
                            ),
                        ),
                        (
                            "permission",
                            models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.permission"),
                        ),
                        (
                            "user",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                            ),
                        ),
                    ],
                    options={
                        "db_table": "bridger_biguserobjectpermission",
                        "abstract": False,
                        "default_related_name": "userobjectpermissions",
                        "unique_together": {("user", "permission", "object_pk")},
                    },
                ),
            ],
        ),
        migrations.AlterModelTable(
            name="groupobjectpermission",
            table=None,
        ),
        migrations.AlterModelTable(
            name="userobjectpermission",
            table=None,
        ),
        migrations.AddIndex(
            model_name="groupobjectpermission",
            index=models.Index(fields=["content_type", "object_pk"], name="wbcore_guar_content_4afd41_idx"),
        ),
        migrations.AddIndex(
            model_name="groupobjectpermission",
            index=models.Index(fields=["content_type", "object_pk", "group"], name="wbcore_guar_content_83dcd4_idx"),
        ),
        migrations.AddIndex(
            model_name="userobjectpermission",
            index=models.Index(fields=["content_type", "object_pk"], name="wbcore_guar_content_138d49_idx"),
        ),
        migrations.AddIndex(
            model_name="userobjectpermission",
            index=models.Index(fields=["content_type", "object_pk", "user"], name="wbcore_guar_content_98fc0f_idx"),
        ),
    ]
