from django.db import models

# Create your models here.


#names

class Name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name