from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.CreateAPIView):
    pass