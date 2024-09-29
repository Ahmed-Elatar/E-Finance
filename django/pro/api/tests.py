from django.test import TestCase
from rest_framework import status
from .views import *
from .models import *
from .serializers import *



class ReceiveTickerDataTest(TestCase):
    
    def test_post_not_accepted(self , data={'status': 'not-accepted'}):
        

        response = data['status']

        self.assertEqual(response, 'not-accepted')

    
    def test_get(self):
        
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        if response.content:  # In case Django sends content with the 204 status
            self.assertJSONEqual(response.content, {"status": "NO-Data-recived"})