from rest_framework import serializers
from SDApp.models.user import CustomUser as CustomUserModel
from SDApp.validators import (
    check_password_strength,
    password_not_strong_enough_message,
)


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["id", "email", "first_name", "last_name", "is_active", "date_joined"]


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=32, write_only=True)
    confirm_password = serializers.CharField(
        min_length=6, max_length=32, write_only=True
    )


class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    password = serializers.CharField()


class CustomUserLoginSerializer(CustomUserSerializer):
    pass


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        min_length=6, max_length=32, write_only=True
    )

    class Meta:
        model = CustomUserModel
        fields = ["email", "first_name", "last_name", "password", "confirm_password"]
        extra_kwargs = {"password": {"write_only": True}}

    @staticmethod
    def validate_password(password):
        if not check_password_strength(password):
            raise serializers.ValidationError(password_not_strong_enough_message)
        return password

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(
                {"confirm_password": "Passwords must match"}
            )
        if CustomUserModel.objects.filter(email=data.get("email")).exists():
            raise serializers.ValidationError({"email": "Email already exists."})
        return data
