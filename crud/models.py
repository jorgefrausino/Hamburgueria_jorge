from django.db import models


class Hamburguer(models.Model):
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Hambúrguer"
        verbose_name_plural = "Hambúrgueres"

    def __str__(self):
        return self.nome
