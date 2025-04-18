from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Customer, Sale, SaleItem
from .serializers import (
    CategorySerializer, ProductSerializer, CustomerSerializer,
    SaleSerializer, SaleItemSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True)
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']

    @action(detail=False)
    def low_stock(self, request):
        threshold = int(request.query_params.get('threshold', 10))
        products = Product.objects.filter(stock__lte=threshold)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

    @action(detail=True)
    def purchase_history(self, request, pk=None):
        customer = self.get_object()
        sales = customer.sales.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'customer']

    def create(self, request, *args, **kwargs):
        # Pass items data to serializer context
        serializer = self.get_serializer(
            data=request.data,
            context={'items': request.data.get('items', [])}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=False)
    def dashboard_stats(self, request):
        total_sales = Sale.objects.filter(status='completed').aggregate(
            total=Sum('total_amount'))['total'] or 0
        top_products = SaleItem.objects.values(
            'product__name').annotate(
            total_quantity=Sum('quantity'),
            total_sales=Sum('total_price')
        ).order_by('-total_sales')[:5]
        recent_sales = Sale.objects.filter(
            status='completed').order_by('-created_at')[:5]

        return Response({
            'total_sales': total_sales,
            'top_products': top_products,
            'recent_sales': SaleSerializer(recent_sales, many=True).data
        })

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sale', 'product']
