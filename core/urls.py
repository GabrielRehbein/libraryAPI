from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('authors.urls')),
    path('api/v1/', include('books.urls')),
    path('api/v1/', include('publishers.urls')),
]
