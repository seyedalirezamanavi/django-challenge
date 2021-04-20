from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.serializers import CharField, DateTimeField, IntegerField

from stadium.models import Stadiums, Tickets
from users.serializers import UsersSerializer

class StadiumSerializer(Serializer):
    # this class serialize the stadiums 
    stadium = CharField(
        required=True, allow_blank=False, max_length=100)
    total_seats = IntegerField(default=1000, min_value=0)
    match_date = DateTimeField()
    teams = CharField(
        required=True, allow_blank=False, max_length=100)
    location = CharField(
        required=True, allow_blank=False, max_length=300)
    
    def create(self, validated_data):
        s = Stadiums(
            **validated_data
        )
        s.save()
        return s


class StadiumListSerializer(ModelSerializer):
    # this class serialize the stadiums lists
    class Meta:
        model = Stadiums
        fields = '__all__'


class StadiumVerSerializer(Serializer):
    # this class serialize the stadiums 
    stadium = CharField(
        required=False, max_length=100)
    total_seats = IntegerField(default=1000, min_value=0)
    match_date = DateTimeField()
    teams = CharField(
        required=False, max_length=100)
    location = CharField(
        required=False, max_length=300)

class TicketSerializer(Serializer):
    reserved_seats = User()
    seat_id = IntegerField()
    # def validate_seat_id(self, instance, data):
    #     if data > instance.total_seats:
    #         raise "the seat # does not exist"
    def create(self, validated_data):
        t = Tickets(
            **validated_data
        )
        t.save()
        return t

