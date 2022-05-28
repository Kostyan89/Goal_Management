from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from core.models import User
from core.serializers import (
    CreateUserSerializer,
    LoginSerializer,
    UserSerializer,
    UpdatePasswordSerializer,
)


def login_model_backend(request, user) -> None:
    login(
        request,
        user=user,
        backend='django.contrib.auth.backends.ModelBackend'
    )


class SignupView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        ret = super().post(request, *args, **kwargs)

        user = User.objects.get(username=ret.data['username'])
        login_model_backend(request, user=user)

        return ret


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs) -> Response:
        user_login: LoginSerializer = self.get_serializer(data=request.data)
        user_login.is_valid(raise_exception=True)
        username = user_login.validated_data['username']
        user = User.objects.get(username=username)
        login_model_backend(request, user=user)
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UpdatePasswordView(UpdateAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        login(request=request, user=user, backend='django.contrib.auth.backends.Model')
        return JsonResponse(data=serializer.data, status=200)
