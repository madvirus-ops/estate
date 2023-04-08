from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail="Requested Profile No dey"


class NotYoutProfile(APIException):
    status_code = 403
    default_detail = "Profile no be your own"

