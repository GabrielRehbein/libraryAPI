from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serialzers import BookSerializer
from core.permissions import GlobalDefaultPermission


class BookListCreateView(ListCreateAPIView):
    permission_classes = [GlobalDefaultPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [GlobalDefaultPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

