from django.contrib.auth.backends import ModelBackend
from SDApp.models.user import CustomUser


class EmailAuth(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if 'username' in kwargs:
            email = kwargs['username']
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
