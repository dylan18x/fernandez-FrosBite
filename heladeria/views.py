from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Sabor, Producto
from .serializer import ProductoSerializer, SaborSerializer
from .permissions import IsAdminOrReadOnly

class SaborViewSet(viewsets.ModelViewSet):
    queryset = Sabor.objects.all().order_by("id")
    serializer_class = SaborSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre"]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related("marca").all().order_by("-id")
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["sabor","estado"]
    search_fields = ["nombre","codigo"]
    ordering_fields = ["precio"]


    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()