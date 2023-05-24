class Computer:
    
    def __init__(self, ram, cpu, storage):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
       

    def turnOn(self):
        print('Computer is turning on...')
        
comp = Computer('4 GB', 'i3', '500 GB')
comp.turnOn()

class Laptop(Computer):
    
    def __init__(self, ram, cpu, storage, screen, touch):
        super().__init__(ram, cpu, storage)
        self.screen = screen
        self.touch = touch
    
    def sleep(self):
        print('Laptop slept ..')
        
        # method overriding for multiple classes (inheritence)
    def turnOn(self):
        print('Laptop is turning on...')
        
lappy = Laptop('8 GB', 'ryzen 5', '1 TB', '1080p', False)
print(lappy.ram)

lappy.turnOn()
        