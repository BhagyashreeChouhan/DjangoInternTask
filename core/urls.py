from django.urls import path
from .views import PublicEndpoint, ProtectedEndpoint

urlpatterns = [
    path("public/", PublicEndpoint.as_view()),
    path("protected/", ProtectedEndpoint.as_view())
]