from django.db import models


class Bloco(models.Model):
    numero = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.numero


class Apartamento(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return "Apartamento " + str(self.numero) + " - " + str(self.bloco)


class Residente(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.PROTECT)
    cpf_cnpj = models.CharField(
        verbose_name="CPF/CNPJ", max_length=18, unique=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    data_inicio = models.DateField(verbose_name="Data de Início do contrato")
    data_fim = models.DateField(verbose_name="Data de Término do contrato")
    numero_cadastro = models.IntegerField(verbose_name="Numero de Cadastro")
    valor_aluguel = models.FloatField(verbose_name="Valor do Aluguel")
    valor_condominio = models.FloatField(verbose_name="Valor do Condomínio")
    outros = models.FloatField(
        verbose_name="Outros valores a pagar", null=True, blank=True)

    def __str__(self):
        return self.nome + " - " + str(self.apartamento)
