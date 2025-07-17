from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from accounts.serializers import LoginSerializer

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)

                response = {
                    "message": f"{user.get_username()} logged in successfully.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                }
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response = {
                    "message": "Invalid Credentials",
                    "data": "Please provide valid email and password.",
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        error_response = {
            "message": "Data Validation Error",
            "data": serializer.errors,
        }
        return Response(data=error_response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)