from enum import Enum
from django.db import models

class StatesEnum(Enum):
    EN_DEPOSITO = 'en_deposito'
    EN_DISTRIBUCION = 'en_distribucion'
    #Otros
    def getStatesEnumChoices():
        return [choice.value for choice in StatesEnum]

class ClassificationAttributes(Enum):
    PESO = 'weight'
    ALTURA = 'height'
    #Otros