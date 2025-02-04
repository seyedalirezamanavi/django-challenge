from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from users.serializers import UserSignupSerializer, UserLoginSerializer



class SignupView(APIView):

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            u = serializer.save()
            return Response({
                'message': 'Account created',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = (permissions.AllowAny,)
    

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
        return super(LoginView, self).post(request, format=None)

