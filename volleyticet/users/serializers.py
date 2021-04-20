from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSignupSerializer(ModelSerializer):
    # this class serialize the users

    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(ModelSerializer):
    # this class serialize the users

    class Meta:
        model = User
        exclude = ['']



class UsersSerializer(ModelSerializer):
    # this class serialize the users

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username']
