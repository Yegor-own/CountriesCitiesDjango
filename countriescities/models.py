from django.db import models

# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Cities(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name