from django.test import TestCase, Client

c = Client()
response = c.get('/officelunchorder/')
response.status_code
# 200
response.content
response = c.post('/officelunchorder/login/')
response.status_code
# 200
response.content
response = c.get('/officelunchorder/logout/')
response.status_code
# 200
response.content