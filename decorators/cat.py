class Feline:
    def __init__(self, name):
        self.name = name
        print('Creating a feline')

    def meow(self):
        print(f'{self.name}: meow')


    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name


#Lion class

class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')



# Tiger class
class Tiger(Feline):
    def __init__(self):
        print('Creating a tiger')

c = Feline('Kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()
l.roar()