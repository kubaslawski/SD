from django.contrib.auth.backends import ModelBackend
from SDApp.models.user import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class EmailAuth(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return str(refresh), str(access)
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
