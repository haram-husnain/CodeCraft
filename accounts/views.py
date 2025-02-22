from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.CreateAPIView):
    pass

#root api/ url
class APIRootView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to the CodeCraft API!',
            'endpoints': {
                'register': '/api/register/',
                'login': '/api/login/',
            }
        })