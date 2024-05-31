from rest_framework import status
from rest_framework.decorators import api_view ,APIView
from rest_framework.response import Response
from base.models import Room ,User
from api.serializers import RoomSerializer ,UserSerializer
from django.http import Http404

from django.shortcuts import get_object_or_404

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/user',
    ]
    return Response(routes)

class Room_Detail(APIView):
    def get(self,request,pk):
        if request.method == 'GET':
            try:
                rooms = get_object_or_404(Room,pk=pk)
                serializer = RoomSerializer(rooms)
                return Response(serializer.data)
            except Http404:
                return Response({'detail':'room not found'} , status=status.HTTP_404_NOT_FOUND)
    def put(self,request):
        if request.method == 'PUT':
            serializer = RoomSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request ,pk):
        rooms =get_object_or_404(Room,pk=pk)
        rooms.delete()
        return Response( {'delete':'Room deleted '},status=status.HTTP_204_NO_CONTENT)

class GetRoom(APIView):
    def get(self,request):
        if request.method == 'GET':
            rooms = Room.objects.all()
            serilizer = RoomSerializer(rooms, many=True)
            return Response(serilizer.data )

    def post(self, request):
        if request.method == 'POST':
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUser(request):
    users=User.objects.all()
    serializer= UserSerializer(users,many=True)
    return Response(serializer.data)