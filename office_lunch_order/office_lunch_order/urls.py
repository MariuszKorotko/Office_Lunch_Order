"""office_lunch_order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from office_lunch_order_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'},
        name='logged-out'),
    url(r'^orders/', OrdersView.as_view(),name='orders'),
    url(r'new_order/', NewOrderView.as_view(), name="new-order"),
    url(r'add_order/(?P<id>(\d)+)', AddOrderView.as_view(),
        name="add-order"),
    url(r'order_details/(?P<id>(\d)+)', OrderDetailsView.as_view(),
        name="order-details"),
    url(r'^close_order/', CloseOrderView.as_view(),
        name="close-order")
]
