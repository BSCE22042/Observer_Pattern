# Base component class
class Coffee:
    def get_description(self):
        return "Basic Coffee"
    
    def get_cost(self):
        return 5.0

# Concrete component
class Espresso(Coffee):
    def get_description(self):
        return "Espresso"
    
    def get_cost(self):
        return 8.0

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_description(self):
        return self.coffee.get_description()
    
    def get_cost(self):
        return self.coffee.get_cost()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", with Milk"
    
    def get_cost(self):
        return self.coffee.get_cost() + 1.5

class CaramelDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", with Caramel"
    
    def get_cost(self):
        return self.coffee.get_cost() + 2.0

class WhippedCreamDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", with Whipped Cream"
    
    def get_cost(self):
        return self.coffee.get_cost() + 1.0

# Client code
if __name__ == "__main__":
    # Simple espresso
    my_coffee = Espresso()
    print(f"{my_coffee.get_description()}: ${my_coffee.get_cost()}")
    
    # Espresso with milk
    my_coffee = MilkDecorator(Espresso())
    print(f"{my_coffee.get_description()}: ${my_coffee.get_cost()}")
    
    # Complex coffee with multiple decorators
    my_coffee = WhippedCreamDecorator(CaramelDecorator(MilkDecorator(Espresso())))
    print(f"{my_coffee.get_description()}: ${my_coffee.get_cost()}")
    
    # Starting with basic coffee and adding decorators
    basic_with_extras = CaramelDecorator(WhippedCreamDecorator(Coffee()))
    print(f"{basic_with_extras.get_description()}: ${basic_with_extras.get_cost()}")