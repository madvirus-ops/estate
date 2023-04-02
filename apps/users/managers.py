from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("valid email required"))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        if not username:
            raise ValueError(_("username not set"))
        if not first_name:
            raise ValueError(_("set firstname"))
        if not last_name:
            raise ValueError(_("set lastname"))

        if email:
            email = self.normalize_email(email)

        else:
            raise ValueError("email must be set")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, username, first_name, email, last_name, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("must be staff"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("must be superuser"))
        if not password:
            raise ValueError(_("must set password"))
        if email:
            email = self.normalize_email(email)
        else:
            raise ValueError("Admin email must be set")

        user = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        return user
