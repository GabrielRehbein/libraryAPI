from django.urls import path
from books.views import BookListCreateView, BookRetrieveUpdateDestroyView


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
    path('books/<uuid:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='books-list-create'),
]
