from abc import ABC, abstractmethod

class MathOperation(ABC): #abstract base class
    @abstractmethod
    def compute(self, a, b):
        pass


class Addition(MathOperation): #concrete subclasses
    def compute(self, a, b):
        return a + b

class Multiplication(MathOperation):
    def compute(self, a, b):
        return a * b
 
class Exponentiation(MathOperation):
    def compute(self, a, b):
        return a ** b
 
operations = [Addition(), Multiplication(), Exponentiation()]
a, b = 3, 9

print(f"Values of a and b are: {a} and {b} ")
for operation in operations:
    print(f"Result of {operation.__class__.__name__} is: {operation.compute(a, b)} ")
