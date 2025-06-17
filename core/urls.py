from django.urls import path
from .views import PublicEndpoint, ProtectedEndpoint, Register, Login

urlpatterns = [
    path("public/", PublicEndpoint.as_view()),
    path("protected/", ProtectedEndpoint.as_view()),
    path("register/", Register.as_view())
]