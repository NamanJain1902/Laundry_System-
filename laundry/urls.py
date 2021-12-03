from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='laundry-index'),
    path('place_order/', views.placeOrder, name='laundry-place-order'),
    path('order_history/', views.orderHistory, name='laundry-order-history'),
    path('orders/', views.allOrders, name='laundry-orders-list'),
    path('userRecord/',views.displayLastOrder, name='display-last-order'),
]