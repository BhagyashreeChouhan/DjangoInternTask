from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

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
