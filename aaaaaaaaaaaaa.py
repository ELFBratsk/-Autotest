class Dog () :
    """Инициализирует атрибуты name и age."""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):

        """Собака садится по команде."""
        print(self.name.title() + " сидит")

    def roll_over(self):
        print(self.name.title() + " перекатывается")


my_dog =Dog('Володя',6)

my_dog.sit()
my_dog.roll_over()
print('Мою собаку зовут ' + my_dog.name)
print('Моей собаке ' + str(my_dog.age) + ' лет')

