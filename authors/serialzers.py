from rest_framework import serializers
from .models import Author, AuthorNationality


class AuthorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorNationalitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = AuthorNationality
        fields = '__all__'