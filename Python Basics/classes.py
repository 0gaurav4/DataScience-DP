class Cat:
    
    name = "Tom"
    color = 'grey'
    height = '30cm'
    
    def eat(self):
        print('cat eats food')
        
    def play(self):
        print('cat play with toys')
     
cat1 = Cat()

print(cat1.name)

cat1.play()

cat2 = Cat()

print(cat1.name)

cat2.play()