from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Running")
#Error u cant create an object for absract
# com = Computer()
lap = Laptop()
lap.process()