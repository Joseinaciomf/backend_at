from django.db import models

class Manga(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    volumes = models.IntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo