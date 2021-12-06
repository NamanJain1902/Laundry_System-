from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='laundry-index'),
    path('place_order/', views.placeOrder, name='laundry-place-order'),
    path('order_history/', views.orderHistory, name='laundry-order-history'),
    path('orders/', views.allOrders, name='laundry-orders-list'),
    path('userRecord/',views.displayLastOrder, name='display-last-order'),
    path('orders/ajax/update-processing/', views.update_processing, name='ajax_update_processing'), # AJAX
    path('orders/ajax/update-delivered/', views.update_delivered, name='ajax_update_delivered'), # AJAX
]
