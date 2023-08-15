from django.db import models
from .enums import *
from .classifiers import *
from .settings import *
from .system import System

import uuid

#Funcion para generar un id de tracking unico para cada paquete
def generateTracking():
    return str(uuid.uuid4())[:20]

#Cliente 
class Client(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
#Receptor o destinatario del paquete
class Recipient(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Package(models.Model):
    tracking = models.CharField(max_length=20, primary_key=True, default=generateTracking)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    height = models.DecimalField(max_digits=7, decimal_places=2)
    state = models.CharField(max_length=15, choices=[(state.value, state.name) for state in StatesEnum], default=DEFAULTPACKAGESTATE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    typePackage = models.CharField(max_length=2, blank=True)
    
    def __str__(self):
        return self.tracking
    
    @staticmethod
    def getFreePackages():
        return Package.objects.filter(formitem=None)

    def save(self, *args, **kwargs):
        if not self.typePackage:
            self.typePackage = System.classifyPackage(self,CLASSIFICATION_MODE)
        super().save(*args, **kwargs)

class Form(models.Model):
    formNumber = models.IntegerField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return str(self.formNumber)

class FailureReason(models.Model):
    reason = models.CharField(max_length=30, primary_key=True)

    @staticmethod
    def getFailureReasons():
        return FailureReason.objects.all() 

    def __str__(self):
        return self.reason

class FormItem(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    position = models.IntegerField()
    failureReason = models.ForeignKey(FailureReason, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('form','position')

    def __str__(self):
        return f"Planilla #{self.form} - Posicion: {self.position}, Paquete: {self.package}, - Estado: {self.package.state} "

