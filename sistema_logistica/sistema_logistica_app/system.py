from .classifiers import *
from .enums import ClassificationAttributes

class System:

    classifiers = []

    @classmethod
    def addClassifier(cls, classifier):
        cls.classifiers.append(classifier)

    @classmethod
    def classifyPackage(cls, package, *args):
        for classifier in cls.classifiers:
            classification = classifier.classify(package, *args)
            if classification:
                return classification
        return None
    
    @classmethod
    def getFreePackages(cls):
        from .models import Package
        return Package.objects.filter(formitem=None)

    @classmethod
    def getFailureReasons(cls):
        from .models import FailureReason
        return FailureReason.objects.all()

# Creo las instancias de los clasificadores para agregarlas al sistema
weightClassifierG = HigherClassifier(attributeValue=3000, classification='G', classificationAttribute=ClassificationAttributes.PESO)
weightClassifierM = LowerClassifier(attributeValue=3000, classification='M', classificationAttribute=ClassificationAttributes.PESO, nextClassifier=weightClassifierG)
weightClassifierP = LowerClassifier(attributeValue=1000, classification='P', classificationAttribute=ClassificationAttributes.PESO, nextClassifier=weightClassifierM)

#Añado al sistema solo una instancia por atributo, en este caso se añadira el clasificador P
#Ya que en caso de el producto no calificar como "P" se irá al siguiente clasificador que será el M y luego al G
System.addClassifier(weightClassifierP)
