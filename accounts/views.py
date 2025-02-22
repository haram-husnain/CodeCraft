from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.CreateAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

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