class Cat:
    
    def __init__(self, name, color, toy, food):
        self.name = name
        self.color = color
        self.toy = toy
        self.food = food
            
    def eat(self):
        print('cat eats '+self.food)
        
    def play(self):
        print('cat play with '+self.toy)
     
cat1 = Cat('Tom', 'grey', 'boll', 'jerry')

print(cat1.name)

cat1.play()
cat1.eat()

cat2 = Cat('Snowbell', 'white', 'stick', 'berry')

print(cat2.name)

cat2.play()
cat2.eat()