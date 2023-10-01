from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from puppies.models import Puppy
from puppies.serializers import PuppySerializer

from django.shortcuts import get_object_or_404


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    puppy = get_object_or_404(Puppy, pk=pk)
    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_puppies(request):
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response({})
