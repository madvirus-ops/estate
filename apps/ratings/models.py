from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.profiles.models import Profile
from apps.common.models import TimeBasedModel
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Rating(TimeBasedModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        User,
        verbose_name=_("The Rater"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="rater",
    )
    agent = models.ForeignKey(
        User,
        verbose_name=_("The Agent"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="agent_review",
    )
    rating = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text="1 = poor <--> 5 = excellent",
    )
    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
