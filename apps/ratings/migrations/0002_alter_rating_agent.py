# Generated by Django 4.1.7 on 2023-04-03 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="agent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="agent_review",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The Agent",
            ),
        ),
    ]
