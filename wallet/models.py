from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.PositiveIntegerField(default=0)


class Transaction(models.Model):
    wallet = models.ForeignKey(to=Wallet, on_delete=models.PROTECT)
    txid = models.TextField(unique=True)
    amount = models.IntegerField()
