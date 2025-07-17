from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import TokenError, RefreshToken

from accounts.serializers import LogOutSerializer

class LogOutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogOutSerializer

    def post(self, request: Request) -> Response:
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                refresh = serializer.data.get('refresh_token')
                token = RefreshToken(refresh)
                token.blacklist()

                response = {
                    "message": "Successfully logged out",
                }
                return Response(data=response, status=status.HTTP_204_NO_CONTENT)
            else:
                error_response = {
                    "message": "Invalid refresh token",
                    "data": serializer.errors
                }
                return Response(data=error_response, status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            response = {
                "message": "Invalid Token",
            }
            return Response(data=response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)