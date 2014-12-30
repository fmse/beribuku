from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    nama = models.CharField(blank=auto)

    class Meta:
        abstract = True

class Program(CommonInfo):
    status = models.BooleanField(default=False)
    deadline = models.DateField(blank=True)
    no_rekening = models.CharField(blank=True)

class Image(CommonInfo):
    program = models.ForeignKey(Program)
    url = models.CharField(blank=True)

class Item(CommonInfo):
    program = models.ForeignKey(Program)

class ProgramItem(CommonInfo):
    program = models.ForeignKey(Program)
    item = models.ForeignKey(Program)

class Donatur(CommonInfo):
    program = models.ForeignKey(Program)
    email = models.CharField(blank=True)

class Admin(CommonInfo):
    username = models.CharField(blank=True)
    password = models.CharField(blank=True)