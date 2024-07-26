from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Publisher
from .serializers import PublisherSerializer
from core.permissions import GlobalDefaultPermission

# Create your views here.
class PublisherListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer