# Implementing the Abstract Factory pattern
# Consider the case of your favorite pizza place.
# It serves multiple types of pizzas, right? 
# Wait, hold on, I know you want to order on right away,
# but let's just get back to the example for now! 
# now, imagine that we create a pizza store 
# where you are served with delicious Indian and American pizzas.
# For this, we first create an abstract base class, PizzaFactory
# (AbstractFactory in the preceding UML diagram)
from abc import ABCMeta, abstractmethod 

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        pass 

    @abstractmethod
    def createNonVegPizza(self):
        pass 

class IndianPizzaFactory(PizzaFactory):
    
    def createVegPizza(self): # createProduct()
        return DeluxVeggiePizza()
    
    def createNonVegPizza(self): # createAnotherProduct()
        return ChickenPizza() 

class USPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return MexicanVegPizza() 
    
    def createNonVegPizza(self): # createAnotherProduct()
        return HamPizza() 

class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass 

# AnotherAbstractProduct
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass 
    
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__ )

# AnotherConcreteProduct2
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, 'is served with Chicken on ', type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)

# AnotherConcreteProduct2
class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, 'is served with Ham on', type(VegPizza).__name__)

class PizzaStore:
    def __init__(self):
        pass 
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory 
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare() 
            self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore() 
pizza.makePizzas()
