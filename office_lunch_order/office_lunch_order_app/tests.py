from django.test import TestCase, Client

c = Client()
response = c.get('/officelunchorder/')
response.status_code # 200
response.content
response = c.post('/officelunchorder/login/')
response.status_code # 200
response.content
response = c.get('/officelunchorder/logout/')
response.status_code # 200
response.content
response = c.get('/officelunchorder/orders/')
response.status_code # 302 found
response = c.get('/officelunchorder/new_order/')
response.status_code # 302 found
response = c.get('/officelunchorder/add_order/25/') # existing order_id
response.status_code # 302 found
response = c.get('/officelunchorder/order_details/25/') # existing order_id
response.status_code # 302 found
response = c.post('/officelunchorder/close_order/')
response.status_code # 302 found

