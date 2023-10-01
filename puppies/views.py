from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from puppies.models import Puppy
from puppies.serializers import PuppySerializer

from django.shortcuts import get_object_or_404


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def get_delete_update_puppy(request, pk):
    puppy = get_object_or_404(Puppy, pk=pk)
    if request.method == 'GET':
        serializer = PuppySerializer(puppy)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = PuppySerializer(puppy, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_post_puppies(request):
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PuppySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
