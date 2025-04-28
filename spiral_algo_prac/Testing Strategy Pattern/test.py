from abc import abstractmethod, ABC

# STRATEGY PATTERN 

class SuperClass(ABC):
    @abstractmethod
    def main(self):
        pass


class SubClass(SuperClass):
    def main(self):
        x = 5
        y = 10
        print(x+y)
        return x + y

class SubClass_2(SuperClass):
    def main(self):
        z = 200
        n = 50
        print(z+n)
        return super().main()

class SubClass_3(SuperClass):
    def main(self):
        j,e = 30,80
        print(j+e)
        return super().main()
    
class Strategy_Pattern: # Switch between strategies (The ability to choose and execute each strategy)
    def __init__(self, strategy: SuperClass):
        self.strategy = strategy
        # Behavior for the Strategy pattern class when its used to set the first pattern. or Sub class.
        self.set_strategy()

    # States 
    def set_strategy(self):
        self.call_strategy = self.strategy

    def execute_strategy(self):
        return self.call_strategy.main()

# it's literally the same thing as instantiating like this:
# func = SuperClass()
# func.main()
# Just separated into more steps/functions.
# func = self.strategy
# self.call_strategy.main() is func.main()

if __name__ == "__main__":
    # Call each strategy dynamically
    situation = Strategy_Pattern(SubClass()) # Choose the first Pattern to set then execute.
    situation.execute_strategy()
