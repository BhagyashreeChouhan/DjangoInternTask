from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import RegisterSerializer
from .tasks import send_welcome_email

# Public endpoint
class PublicEndpoint(APIView):
    """
    A simple public endpoint accessible without authentication.
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({"message": "Hello from public endpoint!"})

# Protected endpoint
class ProtectedEndpoint(APIView):
    """
    Endpoint accessible only to authenticated users using TokenAuthentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello {request.user.username} from protected endpoint!"})

# Registration endpoint
class Register(APIView):
    """
    Handles user registration.
    Sends a welcome email via Celery after successful registration.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email.delay(user.email, user.username)
            response_data = {
                "message": "Registration successful.",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)