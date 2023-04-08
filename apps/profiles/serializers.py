from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "id",
            "phone_number",
            "profile_image",
            "bio",
            "license",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "is_agent",
            "num_reviews",
            "reviews"
        ]
    def get_full_name(self,obj):
        return obj.user.get_fullname()

    def get_reviews(self,obj):
        reviews=obj.agent_review.all()