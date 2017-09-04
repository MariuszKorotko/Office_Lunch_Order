from django.test import TestCase, Client

c = Client()
response = c.get('/officelunchorder/')
print(response.status_code)
print(response.content)