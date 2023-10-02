from rest_framework import viewsets
from .models import Product
from rest_framework import filters
from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)

        month_offer = self.request.query_params.get('month_offer', None)
        if month_offer:
            queryset = queryset.filter(month_offer=month_offer)

        availability = self.request.query_params.get('is_available', None)
        if availability:
            queryset = queryset.filter(availability=availability)

        pickup = self.request.query_params.get('pickup', None)
        if pickup:
            queryset = queryset.filter(pickup=pickup)

        return queryset