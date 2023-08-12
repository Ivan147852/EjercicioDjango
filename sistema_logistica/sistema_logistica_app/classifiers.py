# En el archivo classifiers.py

from abc import ABC, abstractmethod

class PackageClassifier:
    
    def __init__(self, nextClassifier=None):
        self.nextClassifier = nextClassifier

    def setNextClassifier(self, nextClassifier):
        self.nextClassifier = nextClassifier

    @abstractmethod
    def classify(self, package):
        pass

class SimpleClassifier(PackageClassifier):
    def __init__(self, attributeValue, classification, classificationAttribute , nextClassifier=None):
        super().__init__(nextClassifier)
        self.attributeValue = attributeValue
        self.classification = classification
        self.classificationAttribute = classificationAttribute

class CompositeClassifier(PackageClassifier):
    def __init__(self, classifier1, classifier2, classification, nextClassifier=None):
        super().__init__(nextClassifier)
        self.classifier1 = classifier1
        self.classifier2 = classifier2
        self.classification = classification


class LowerClassifier(SimpleClassifier):
    
    def classify(self, package, *args):
        for attribute in args:
            if attribute == self.classificationAttribute.value:
                if getattr(package, self.classificationAttribute.value) < self.attributeValue:
                    return self.classification
                elif self.nextClassifier:
                    return self.nextClassifier.classify(package,*args)
        return None

class HigherClassifier(SimpleClassifier):

    def classify(self, package, *args):
        for attribute in args:
            if attribute == self.classificationAttribute.value:
                if getattr(package, self.classificationAttribute.value) > self.attributeValue:
                    return self.classification
                elif self.nextClassifier:
                    return self.nextClassifier.classify(package,*args)
        return None

class EqualClassifier(SimpleClassifier):

    def classify(self, package, *args):
        for attribute in args:
            if attribute == self.classificationAttribute.value:
                if getattr(package, self.classificationAttribute.value) > self.attributeValue:
                    return self.classification
                elif self.nextClassifier:
                    return self.nextClassifier.classify(package,*args)
        return None

class AndClassifier(CompositeClassifier):

    def classify(self, package, *args):
        if (self.classifier1.classify(package, *args) != None) and (self.classifier2.classify(package, *args)):
            return self.classification
        elif self.nextClassifier:
            return self.nextClassifier.classify(package,*args)
        return None

class OrClassifier(CompositeClassifier):

    def classify(self, package, *args):
        if (self.classifier1.classify(package, *args) != None) or (self.classifier2.classify(package, *args)):
            return self.classification
        elif self.nextClassifier:
            return self.nextClassifier.classify(package,*args)
        return None

