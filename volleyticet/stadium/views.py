from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


from stadium.models import Stadiums
from stadium.serializers import StadiumSerializer, StadiumListSerializer
# from stadium.serializers import TicketSerializer
from users.serializers import UsersSerializer



class AddStadiumView(APIView):

    def post(self, request):
        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            s = serializer.save()
            return Response({
                'message': 'Stadium created',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        serializer = StadiumListSerializer(data=request.data)
        if serializer.is_valid():
            stadiums = Stadiums.objects
            if 'stadium' in request.data:
                stadiums = stadiums.filter(
                    stadium=serializer.data['stadium']
                )
            if 'teams' in request.data:
                stadiums = stadiums.filter(
                    teams=serializer.data['teams']
                )

            serializer = StadiumSerializer(instance=stadiums, many=True)
            return Response(
                {
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class SeatsView(APIView):

    def post(self, request):
        pass
#         # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)
#         # permission_classes = (IsAuthenticated,)
#         print( request.data)
#         stadium = Stadiums.objects.filter(stadium = request.data['stadium'])
#         print(stadium)
#         serializer = TicketSerializer(data=request.data, instance = stadium)
#         if serializer.is_valid():
#             s = serializer.save()
#             return Response({
#                 'message': 'ticket reserved',
#                 'data': serializer.data
#             })
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

    def get(self, request):
        pass
