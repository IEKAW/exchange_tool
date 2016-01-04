from django.db import models
from django.utils import timezone
import pandas as pd


class ExchangeDetail(models.Model):
    order_id = models.IntegerField(null=True)
    currency_pair = models.CharField(max_length=255, null=True)
    exchange_date = models.DateTimeField(null=True)
    method = models.CharField(max_length=255, null=True)
    trade_section = models.CharField(max_length=255, null=True)
    lot = models.IntegerField(null=True)
    contract_price = models.FloatField(null=True)
    trade_profit = models.IntegerField(null=True)
    settlement_profit = models.FloatField(null=True)


class kessai(models.Model):
    order_id = models.IntegerField(null=True)
    contract_date = models.DateTimeField(null=True)
    kendama_num = models.CharField(null=True, max_length=255)
    currency_pair = models.CharField(null=True, max_length=255)
    trade_method = models.CharField(null=True, max_length=255)
    amount = models.IntegerField(null=True)
    settlement_price = models.FloatField(null=True)
    tatal_sw = models.IntegerField(null=True)
    realized_profit = models.IntegerField(null=True)
    total_loss = models.IntegerField(null=True)
