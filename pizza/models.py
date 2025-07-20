from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table = "pizza"
    name = models.CharField(max_length=20)
    sauces=models.BooleanField(default=False)
    price = models.IntegerField()

