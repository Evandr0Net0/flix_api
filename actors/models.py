from django.db import models

NATIOTALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIOTALITY_CHOICES,
        blank=True,
        null=True
        )
    
    def __str__(self):
        return self.name
    
