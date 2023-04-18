from django.db import models

#Criando a classe que representará Item

class Item(models.Model):

    idItem = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    pontos = models.IntegerField()


# Criando a classe que representará Inventário 

class Inventario(models.Model):
    idInventario = models.IntegerField(primary_key=True)
    manipular = models.BooleanField()
    item_idItem = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="inventario_item")

#Criando a Classe que representará O relacionamento Item por Inventário

class Inventario_tem_Item(models.Model):
    inventario_idInventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name="inventario_tem_item")
    inventario_Item_idItem = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_esta_no_inventario")
    item_idItem = models.IntegerField(primary_key=True)
    quantidade = models.IntegerField()

#Criando a classe que representará Sobrevivente

class Sobrevivente(models.Model):
    idSobrevivente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    ultimo_local = models.DecimalField(max_digits=5, decimal_places=2)
    infectado = models.BooleanField()
    inventario_idInventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name="sobrevivente_inventario")
    inventario_Item_idItem = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="sobrevivente_inventario_item")


