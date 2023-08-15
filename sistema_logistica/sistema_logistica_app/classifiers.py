# En el archivo classifiers.py

from abc import abstractmethod

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

    def classify(self, package, *args):
        for attribute in args:
            if attribute == self.classificationAttribute.value:
                if self.compare(getattr(package, self.classificationAttribute.value)):
                    return self.classification
                elif self.nextClassifier:
                    return self.nextClassifier.classify(package, *args)
        return None
    
    @abstractmethod
    def compare(self, attribute_value):
        pass

class LowerClassifier(SimpleClassifier):
    def compare(self, attribute_value):
        return attribute_value < self.attributeValue

class HigherClassifier(SimpleClassifier):
    def compare(self, attribute_value):
        return attribute_value > self.attributeValue

class EqualClassifier(SimpleClassifier):
    def compare(self, attribute_value):
        return attribute_value == self.attributeValue
    

class CompositeClassifier(PackageClassifier):
    def __init__(self, classifier1, classifier2, classification, nextClassifier=None):
        super().__init__(nextClassifier)
        self.classifier1 = classifier1
        self.classifier2 = classifier2
        self.classification = classification
    
    def _classify_logic(self, package, *args, operator):
        result1 = self.classifier1.classify(package, *args)
        result2 = self.classifier2.classify(package, *args)
        if (result1 is not None) and operator(result2):
            return self.classification
        elif self.nextClassifier:
            return self.nextClassifier.classify(package, *args)
        return None

class AndClassifier(CompositeClassifier):
    def classify(self, package, *args):
        return self._classify_logic(package, *args, operator=lambda x: bool(x))

class OrClassifier(CompositeClassifier):
    def classify(self, package, *args):
        return self._classify_logic(package, *args, operator=lambda x: not bool(x))
