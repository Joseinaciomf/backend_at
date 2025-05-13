from django.db import models

class Manga(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    volumes = models.IntegerField()
    status = models.CharField(max_length=50, default='Disponível')
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo