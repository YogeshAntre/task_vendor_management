from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Vendor, PurchaseOrder

from django.utils import timezone
from django.db.utils import IntegrityError
from django.db import transaction
from django.urls import reverse
import json
from rest_framework.test import APIClient
from django.test import TestCase,RequestFactory
#Unit test cases for Vendor 

class ProjectTestCase(TestCase):
        
    def setUp(self):

        self.vendor = Vendor.objects.create (id=1,name= 'Test Vendor', contact_details= 'test@example.com', 
        address='123 Test St', vendor_code= 'TEST001', on_time_delivery_rate= 0.0,quality_rating_avg= 10.0,
    average_response_time= 0.0,fulfillment_rate= 0.0)
    
        self.user = User.objects.create(username='admin')


    def test_01_vendor_get_one(self):
        """
            Verify the backend get call on project
        """
        response = self.client.get('http://127.0.0.1:8000/api/vendors/1/')
        self.assertEqual(response.status_code, 200)        
        data = json.loads(response.content)
        print('data',data)
        self.assertEqual(data['name'], 'Test Vendor')

        response = self.client.get('http://127.0.0.1:8000/api/vendors/88/')
        self.assertEqual(response.status_code, 404)
        
    def test_02_post_vendor_view(self):
        """
            Request all project fields are stored in the backend 
        """
        response = self.client.get('http://127.0.0.1:8000/api/vendors/')
        self.assertEqual(response.status_code, 200)
        project = json.loads(response.content)
        print('*******************',project)
        self.assertEqual(len(project), 1)        

        #check project keys from data
        self.assertTrue('id' in project[0].keys())
        self.assertTrue('name' in project[0].keys())
        self.assertTrue('contact_details' in project[0].keys())
        self.assertTrue('address' in project[0].keys())
        self.assertTrue('vendor_code' in project[0].keys())
        self.assertTrue('on_time_delivery_rate' in project[0].keys())
        self.assertTrue('quality_rating_avg' in project[0].keys())
        self.assertTrue('average_response_time' in project[0].keys())
        self.assertTrue('fulfillment_rate' in project[0].keys())
    def test_03_vendors_delete(self):
        """
            Request delete the vendors stored in the backend
        """
        self.factory = RequestFactory()
        self.client = APIClient()
        test= self.client.force_authenticate(user=self.user)
        response = self.client.delete('http://127.0.0.1:8000/api/vendors/1/')
        self.assertEqual(response.status_code, 204)
        #Verify the able to get deleted vendor throws 404
        response = self.client.get('http://127.0.0.1:8000/api/vendors/1/')
        self.assertEqual(response.status_code, 404)
 