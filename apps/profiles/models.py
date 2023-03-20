from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeBasedModel

# Create your models here.

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male",_("Male")
    FEMALE = "Female",_("Female")
    OTHER = "Other",_("Other")


class Profile(TimeBasedModel):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name =_("Phone Number"),
        max_length=30,
        default="+4454546575")
    bio = models.TextField(verbose_name=_("About me"),default="WHo you be?")
    license = models.CharField(verbose_name=_("Your license"),max_length=20,blank=True,null=True)
    profile_image = models.ImageField(verbose_name=_("profile image"),default="/people.jpg")
    gender = models.CharField(verbose_name=_("Your gender"),choices=Gender.choices,default=Gender.OTHER,max_length=20)
    country = CountryField(verbose_name=_("country"),max_length=75,default="NG",blank=False,null=False)
    city = models.CharField(verbose_name=_("City"),max_length=180,default="Lagos",blank=False,null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"),default=False,help_text=_("Are You a Buyer"))
    is_seller = models.BooleanField(verbose_name=_("Seller"),default=False,help_text=_("Are You a Seller"))
    is_agent = models.BooleanField(verbose_name=_("Agent"),default=False,help_text=_("Are You an Agent"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"),default=False)
    rating = models.DecimalField(max_digits=4,default=1,decimal_places=2,null=True,blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Reviews"),default=0,null=True,blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"
