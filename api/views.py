from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import Error
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import SampleModel
from api.serializers import SampleSerializer


@api_view(['GET'])
def sample_list(request):
    if request.method == 'GET':
        samples = SampleModel.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    return HttpResponse(status=405)


@api_view(['GET'])
def sample_detail(request, pk):
    if request.method == 'GET':
        try:
            sample = SampleModel.objects.get(pk=pk)
        except SampleModel.DoesNotExist:
            return HttpResponse(status=404)

        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    return HttpResponse(status=405)


@api_view(['POST'])
@csrf_exempt
def new_sample(request):
    if request.method == 'POST':
        post_data = JSONParser().parse(request)
        serializer = SampleSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(status=405)


@api_view(['DELETE'])
@csrf_exempt
def delete_sample(request, pk):
    try:
        sample = SampleModel.objects.get(pk=pk)
    except SampleModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        sample.delete()
        return Response("OK",status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)
