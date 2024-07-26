from django.db import models


CONTRY_ORIGIN = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('FRA', 'França'),
    ('JP', 'Japão'),
    ('DE', 'Alemanha'),
    ('ITA', 'Itália'),
)

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    founded = models.IntegerField(blank=True, null=True)
    contry_origin = models.CharField(choices=CONTRY_ORIGIN, max_length=4)


    def __str__(self) -> str:
        return self.name