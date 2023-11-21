from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=2, decimal_places=1, default=0.0,validators=[MinValueValidator(0.0,message = "Rate from 0 to 5."),MaxValueValidator(5.0)])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie_edit', kwargs={'pk': self.pk})