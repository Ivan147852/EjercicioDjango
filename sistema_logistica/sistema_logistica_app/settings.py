""" Configuracion del proyecto:
Aqui se encuentra las variables que pueden utilizarse para configurar diferentes aspectos del proyecto
Por ejemplo, el modo de clasificacion, el estado default del paquete, los limites de peso para la clasificacion, etc
"""

import sys

CLASSIFICATION_MODE = ["weight"]

from .enums import StatesEnum
DEFAULT_PACKAGE_STATE = StatesEnum.EN_DEPOSITO

THRESHOLD_LIGHT_WEIGHT = 1000
THRESHOLD_MEDIUM_WEIGHT = 3000
THRESHOLD_HEAVY_WEIGHT = sys.maxsize
