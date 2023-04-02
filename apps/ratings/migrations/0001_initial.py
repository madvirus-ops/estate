# Generated by Django 4.1.7 on 2023-03-27 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "Poor"),
                            (2, "Fair"),
                            (3, "Good"),
                            (4, "Very Good"),
                            (5, "Excellent"),
                        ],
                        help_text="1 = poor <--> 5 = excellent",
                        verbose_name="Rating",
                    ),
                ),
                ("comment", models.TextField(verbose_name="Comment")),
                (
                    "agent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="agent",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="The Agent",
                    ),
                ),
                (
                    "rater",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rater",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="The Rater",
                    ),
                ),
            ],
            options={
                "unique_together": {("rater", "agent")},
            },
        ),
    ]