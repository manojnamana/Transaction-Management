from django.urls import path
from .views import TransactionListCreateAPIView, TransactionDetailAPIView

urlpatterns = [
    path('api/transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('api/transactions/<int:transaction_id>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
]
