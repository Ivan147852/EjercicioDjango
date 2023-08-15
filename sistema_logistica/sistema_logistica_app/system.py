from .classifiers import *
from .enums import ClassificationAttributes, ClassificationValues
from .settings import THRESHOLD_LIGHT_WEIGHT, THRESHOLD_MEDIUM_WEIGHT, THRESHOLD_HEAVY_WEIGHT
 
class System:

    classifiers = []

    @classmethod
    def addClassifier(cls, classifier):
        cls.classifiers.append(classifier)

    @classmethod
    def classifyPackage(cls, package, classificationMode):
        for classifier in cls.classifiers:
            classification = classifier.classify(package, classificationMode)
            if classification:
                return classification
        return None

# Creo las instancias de los clasificadores para agregarlas al sistema
weightClassifierG = LowerClassifier(attributeValue=THRESHOLD_HEAVY_WEIGHT, classification=ClassificationValues.PESO_GRANDE.value, classificationAttribute=ClassificationAttributes.PESO.value)
weightClassifierM = LowerClassifier(attributeValue=THRESHOLD_MEDIUM_WEIGHT, classification=ClassificationValues.PESO_MEDIANO.value, classificationAttribute=ClassificationAttributes.PESO.value, nextClassifier=weightClassifierG)
weightClassifierP = LowerClassifier(attributeValue=THRESHOLD_LIGHT_WEIGHT, classification=ClassificationValues.PESO_PEQUENIO.value, classificationAttribute=ClassificationAttributes.PESO.value, nextClassifier=weightClassifierM)

#Añado al sistema solo una instancia por atributo, en este caso se añadira el clasificador P
#Ya que en caso de el producto no calificar como "P" se irá al siguiente clasificador que será el M y luego al G
System.addClassifier(weightClassifierP)
