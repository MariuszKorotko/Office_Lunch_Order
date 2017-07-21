from django.conf.urls import url
from django.contrib.auth import views as auth_views
from office_lunch_order_app.views import *

app_name = 'office_lunch_order_app'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'office_lunch_order/login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'office_lunch_order/logged_out.html'},
        name='logged-out'),
    url(r'^orders/$', OrdersView.as_view(),name='orders'),
    url(r'^new_order/$', NewOrderView.as_view(), name="new-order"),
    url(r'^add_order/(?P<id>(\d)+)/$', AddOrderView.as_view(),
        name="add-order"),
    url(r'^order_details/(?P<id>(\d)+)/$', OrderDetailsView.as_view(),
        name="order-details"),
    url(r'^close_order/$', CloseOrderView.as_view(),
        name="close-order"),
]