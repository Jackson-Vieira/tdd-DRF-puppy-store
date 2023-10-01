from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from puppies.models import Puppy
from puppies.serializers import PuppySerializer

from django.shortcuts import get_object_or_404


@api_view(['GET', 'DELTE', 'PUT'])
def get_delete_update_puppy(request, pk):
    puppy = get_object_or_404(Puppy, pk=pk)
    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'GET':
        return Response({})


def get_post_puppies(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({})
