from enum import Enum
from django.db import models

class StatesEnum(Enum):
    EN_DEPOSITO = 'en_deposito'
    EN_DISTRIBUCION = 'en_distribucion'
    #Otros

class ClassificationAttributes(Enum):
    PESO = 'weight'
    ALTURA = 'height'
    #Otros