from django.urls import path
from accounts.views import RegisterView, LoginView, APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]