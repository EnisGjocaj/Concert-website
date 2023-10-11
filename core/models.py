from django.db import models

# Create your models here.
class RegisterModel(models.Model):

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
