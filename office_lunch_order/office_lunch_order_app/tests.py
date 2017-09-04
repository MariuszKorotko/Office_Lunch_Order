from django.test import TestCase, Client

c = Client()
response = c.get('/officelunchorder/')
response.status_code
response.content
response = c.post('/officelunchorder/login/')
response.status_code
response.content
