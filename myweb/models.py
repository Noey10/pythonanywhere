from django.db import models


class Cactus(models.Model):
    cactusName = models.CharField(max_length=200)
    cactusPrice = models.IntegerField(default=0)
    amout = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.cactusName} - {self.cactusPrice} - {self.amout}'
