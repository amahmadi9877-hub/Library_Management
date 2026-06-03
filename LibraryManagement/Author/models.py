from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    published_books_count = models.IntegerField(default=0)

    def __int__(self):
        return f"{self.first_name} {self.last_name}"