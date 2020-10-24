from django.db import models


class Cactus(models.Model):
    id = models.AutoField(primary_key=True)
    cactusName = models.CharField(max_length=200)
    cactusPrice = models.IntegerField(default=0)
    amout = models.IntegerField(default=0)
    img = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.id} - {self.cactusName} - {self.cactusPrice} - {self.amout} - {self.img}'


