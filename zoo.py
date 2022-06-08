class Animal:
    def __init__(self, name, health_level, happiness_level) -> None:
        self.name = name
        self.age = 0
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        print (f"Name : {self.name} | health : {self.health_level} | Happiness : {self.happiness_level}")
        return self

    def feed(self):
        self.health_level +=10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, health_level = 100, happiness_level =40)
        self.type = "Lion"

    def feed(self):
        self.health_level += 20
        self.happiness_level += 5
        return self

class Tiger(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, health_level = 80, happiness_level =70)
        self.type = "Tiger"
    
    def feed(self):
        self.health_level += 5
        self.happiness_level += 5
        return self

class Bear(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, health_level = 90, happiness_level =150)
        self.type = "Bear"

    def feed(self):
        self.health_level += 15
        self.happiness_level += 20
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
        return self
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self
zoo1 = Zoo("John's Zoo").add_lion("Nala").add_lion("Simba").add_tiger("Rajah").add_tiger("Shere Khan").print_all_info()