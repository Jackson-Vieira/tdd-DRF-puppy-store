from django.db import models
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Puppy(BaseModel):
    name = models.CharField(max_length=255)
    age = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def get_breed(self):
        return f'{self.name} belongs to {self.breed} breed'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "puppy"
        verbose_name_plural = "puppies"
