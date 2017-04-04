import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import SampleModel
from api.serializers import SampleSerializer

# Create your tests here.

class SampleTest(APITestCase):
    
    def test_sample_creation(self):
        """
            Test sample creation
        """
        data = {'description': 'TestCase', 'value_x': 1.0, 'value_y': 0.1}
        response = self.client.post('/api/sample/new', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SampleModel.objects.count(),1)
   
    def test_sample_list(self):
        """
           Test sample list method
        """
        self.test_sample_creation()
        response = self.client.get('/api/samples/')
        self.assertEqual(len(response.data), SampleModel.objects.count())

    def test_sample_detail(self):
        """
           Test sample detail method
        """
        self.test_sample_creation()
        response = self.client.get('/api/samples/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_sample_delete(self):
        """
           Test sample delete method
        """
        self.test_sample_creation()
        response = self.client.delete('/api/sample/delete/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SampleModel.objects.count(), 0)
