
from django.urls import path
from .views import (
    VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView,
    PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView,
    HistoricalPerformanceListCreateAPIView, HistoricalPerformanceRetrieveUpdateDestroyAPIView,
    VendorPerformanceAPIView,AcknowledgePurchaseOrderAPIView
)
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # Vendor URLs
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor_list'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),

    # Purchase Order URLs
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase_orde_create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder_detail'),

    # Historical Performance URLs
    path('historical_performance/', HistoricalPerformanceListCreateAPIView.as_view(), name='hist_performanc_create'),
    path('historical_performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDestroyAPIView.as_view(), name='historical_performance_detail'),
    #vendor ,purchase order acknowledge
    path('vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor_performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge_purchaseorder'),
    #Token Authentications
    path('get_token/',ObtainAuthToken.as_view())
]
