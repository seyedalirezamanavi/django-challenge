from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField

class UserSignupSerializer(ModelSerializer):
    # this class serialize the users

    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(ModelSerializer):
    # this class serialize the users

    class Meta:
        model = User
        exclude = ['']