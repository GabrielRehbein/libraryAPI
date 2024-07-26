from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')

#melhorar isso -> authors/nationality tenta buscar algo em authors
router.register('authors-nationality', AuthorNationalityViewSet, basename='authors-nationality')

urlpatterns = [
    path('', include(router.urls)),
]