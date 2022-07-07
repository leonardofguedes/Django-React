from django.db import models

class Imovel(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField()
    valor = models.DecimalField(decimal_places=2, max_digits=18)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.nome
