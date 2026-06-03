from django.db import models
from Author.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, max_length=200)
    published_date = models.DateField()
    isbn = models.IntegerField(max_length=13)

    def __str__(self):
        return self.title