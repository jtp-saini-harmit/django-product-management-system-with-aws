from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, CustomerViewSet,
    SaleViewSet, SaleItemViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sale-items', SaleItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Available endpoints:
# /api/categories/ - List and create categories
# /api/categories/{id}/ - Retrieve, update, delete category
# /api/categories/{id}/products/ - List products in category

# /api/products/ - List and create products
# /api/products/{id}/ - Retrieve, update, delete product
# /api/products/low_stock/ - List products with low stock

# /api/customers/ - List and create customers
# /api/customers/{id}/ - Retrieve, update, delete customer
# /api/customers/{id}/purchase_history/ - Get customer's purchase history

# /api/sales/ - List and create sales
# /api/sales/{id}/ - Retrieve, update, delete sale
# /api/sales/dashboard_stats/ - Get sales dashboard statistics

# /api/sale-items/ - List and create sale items
# /api/sale-items/{id}/ - Retrieve, update, delete sale item
