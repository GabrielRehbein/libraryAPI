from rest_framework import viewsets
from .models import Author, AuthorNationality
from .serialzers import AuthorSerialzer, AuthorNationalitySerialzer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission



class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,GlobalDefaultPermission]
    queryset = Author.objects.all()
    serializer_class = AuthorSerialzer


class AuthorNationalityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,GlobalDefaultPermission]
    queryset = AuthorNationality.objects.all()
    serializer_class = AuthorNationalitySerialzer
