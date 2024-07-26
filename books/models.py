import uuid
from django.db import models
from publishers.models import Publisher
from authors.models import Author

TYPE_BOOKS = (
    ('Livro', 'Livro'),
    ('Manga', 'Manga'),
    ('LightNovel', 'LightNovel'),
    ('Novel', 'Novel'),
    ('HQ', 'HQ'),
)

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_BOOKS, max_length=20, default='Livro')
    author = models.ManyToManyField(Author, related_name='books')


    def __str__(self) -> str:
        return self.title