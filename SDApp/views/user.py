from SDApp.serializers import (
    CustomUserLoginSerializer,
    CustomUserRegisterSerializer
)
from SDApp.models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from SDApp.auth.auth import EmailAuth
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class CustomUserRegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            raw_password = serializer.validated_data["password"]
            email = serializer.validated_data["email"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]

            user = CustomUser(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(raw_password)
            user.save()

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLoginView(APIView):
    permission_classes = []
    auth = EmailAuth()

    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = self.auth.authenticate(request, email, password)
            if user:
                refresh_token = RefreshToken.for_user(user)
                access_token = AccessToken.for_user(user)
                return Response(
                    {"refresh_token": str(refresh_token), "access_token": str(access_token)},
                    status=status.HTTP_200_OK,
                )

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
