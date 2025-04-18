from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, CustomerViewSet,
    SaleViewSet, SaleItemViewSet, DashboardView,
    ProductListView, ProductCreateView, ProductUpdateView,
    ProductDeleteView
)

app_name = 'products'

# API Routes
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sale-items', SaleItemViewSet)

urlpatterns = [
    # Template Views
    path('', DashboardView.as_view(), name='dashboard'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
    # API Routes
    path('api/', include(router.urls)),
]

# Available API endpoints:
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

# Available template views:
# / - Dashboard view
# /products/ - Product list view
# /products/create/ - Create new product
# /products/<id>/edit/ - Edit existing product
# /products/<id>/delete/ - Delete product
