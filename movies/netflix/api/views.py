from rest_framework.response import Response
from netflix.models import Movie
from .serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
@api_view(["GET",])
def index(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(instance=movies,many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)

@api_view(['POST',])
def create(request):
    serializer=MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'success':True,
            'message':'movies has been created suuccessfully'
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'success':False,
        'message':serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

class MovieList(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieCreate(generics.CreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieUpdate(generics.UpdateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    model=Movie
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer