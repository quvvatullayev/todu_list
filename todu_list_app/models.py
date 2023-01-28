from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.username

class Todu(models.Model):
    user = models.ForeignKey(User, models.Case, related_name='todu')
    title = models.CharField(max_length=200)
    discreption = models.CharField(max_length=50)
    chekt = models.BooleanField(blank=False)
