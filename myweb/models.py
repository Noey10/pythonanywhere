from django.db import models


class Cactus(models.Model):
    id = models.AutoField(primary_key=True)
    cactusName = models.CharField(max_length=200)
    cactusPrice = models.IntegerField(default=0)
    amout = models.IntegerField(default=0)
    img = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.id} - {self.cactusName} - {self.cactusPrice} - {self.amout} - {self.img}'


class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    status = models.BooleanField(default="False",blank=True)

    def __str__(self):
        return f'Firstname = [ {self.Firstname} ] , Lastname = [ {self.Lastname} ] , ID = [ {self.username} ] , Password = [ {self.password} ] , Email = [ {self.email} ] ,SuperUser = [ {self.status} ]'


