from django.db import models


class AuthorNationality(models.Model):
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return self.nationality


class Author(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey(AuthorNationality, on_delete=models.PROTECT, related_name='author', null=True, blank=True)

    def __str__(self):
        return self.name


#fiz só o model, fazer todo resto
