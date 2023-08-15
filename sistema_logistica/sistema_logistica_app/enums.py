""" Enumerados del proyecto:
Aqui se encuentran las listas de valores predefinidos del proyecto, para evitar las constantes en codigo y
facilitar la comprension del codigo
""" 

from enum import Enum
from django.db import models

class StatesEnum(Enum):
    EN_DEPOSITO = 'en_deposito'
    EN_DISTRIBUCION = 'en_distribucion'
    
    def getStatesEnumChoices():
        return [choice.value for choice in StatesEnum]

class ClassificationAttributes(Enum):
    PESO = 'weight'
    ALTURA = 'height'

class ClassificationValues(Enum):
    PESO_GRANDE = 'G'
    PESO_MEDIANO = 'M'
    PESO_PEQUENIO = 'P'
    