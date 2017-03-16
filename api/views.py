from django.views.decorators.csrf import csrf_exempt
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
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def sample_detail(request, pk):
    if request.method == 'GET':
        try:
            sample = SampleModel.objects.get(pk=pk)
        except SampleModel.DoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', 'PUT'])
@csrf_exempt
def new_sample(request):
    post_data = JSONParser().parse(request)
    serializer = SampleSerializer(data=post_data)
    if request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT' and post_data["id"]:
            sample = SampleModel.objects.get(pk=post_data["id"])
            serializer = SampleSerializer(sample, data=post_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@csrf_exempt
def delete_sample(request, pk):
    try:
        sample = SampleModel.objects.get(pk=pk)
    except SampleModel.DoesNotExist:
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        sample.delete()
        return Response("OK", status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)
