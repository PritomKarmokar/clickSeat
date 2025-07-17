from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.serializers import SignupSerializer
from applibs.logging_utils import get_logger

logger = get_logger(__name__)

class SignUpAPIView(APIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Account Signup Successful",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            error_response = {
                "message": "Signup Failed",
                "data": serializer.errors
            }
            logger.error({"Serializer Error": repr(serializer.errors)})
            return Response(data=error_response, status=status.HTTP_400_BAD_REQUEST)