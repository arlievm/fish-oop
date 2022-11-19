# Задание 1
# Задание 1
# Создайте аналог телефонной книги. Каждая запись в книге должна иметь идентификационный
# номер, имя, фамилия, дату рождения, профессию. Напишите для этого класса метод get_information 
# которая будет выдавать информацию об экземпляре этого класса.
from datetime import date

class Book:
    def __init__(self, ident, first_name, last_name, birth_date, profession):
        self.ident = ident
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.profession = profession
    
    def get_information(self):
        return f'ID: {self.ident}\nFirst_name: {self.first_name}\nLast_name: {self.last_name}\nBirth_date: {self.birth_date}\nProfession: {self.profession}'

c = Book(78887, 'Mukhamed', 'Arliev', date(day=5, month=3, year=2000), 'translation_chinese')
print(c.get_information())


# Задание 2
# Создайте иерархию классов для описания фауны со следующими требованиями:

# Обязательное присутствие классов птиц, рыбы и млекопитающих. Напишите для них методы и парамметры свойственные для животных этих классов. 
# Так же обязательное присутствие классов хищников и травоядных. У классов хищник и травоядное обязательно должен быть метод eat. 
# Этот метод должен показывать, чем питается животное.
# Создайте классы сокол, пингвин, форель, кит. Наследуйте эти классы от вышеуказанных классов, при наследовании обратите внимание  
# на природные свойства животных этих классов. Если есть необходимость, перепишите методы родителя для того чтобы эти методы соответствовали 
# свойствам животного. Создайте экземпляры классов сокол, пингвин, форель, кит. 
# Вызовите все доступные им методыclass Birds:
class Birds:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat worms'


    def swim(self):
        return f'I cannot swim'


    def fly(self):
        return f'I cannot fly'


class Mammals:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat grass'

    def swim(self):
        return f'I cannot swim'


    def fly(self):
        return f'I cannot fly'

class Fishes:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat worms'


    def swim(self):
        return f'I can swim'


    def fly(self):
        return f'I cannot fly'

class Falcon(Birds):
    def eat(self):
        return f'I am eat meat'


class Penquin(Birds):
    def eat(self):
        return f'I am eat fish'

    def swim(self):
        return f'I can swim'

    def fly(self):
        return f'I cannot fly'

class Trout(Fishes):
    def eat(self):
        return f'I am eat korm'
    

class Whale(Fishes):
    def eat(self):
        return f'I am eat planktons'

    def swim(self):
        return f'I can swim'

    
ping = Penquin('royal', 9)
print(ping.eat())
print(ping.swim())
print(ping.fly())

# Задание 3
# Вам дана функция:

# def show_even_numbers(*args): even_numbers_lst = [] 
# for i in args: try: if i%2 == 0: even_numbers_lst.append(i) except TypeError: continue return even_numbers_lst
# Напишите декоративную функцию для этой функции 
# чтобы выводить каждое чётное число введённое в эту функцию раздельно, а так же указывать каким номером вы их получили.

# Пример выходных данных:

# >>>show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)
# 1 - 8
# 2 - 100
# 3 - 12
def show_even_numbers(*args):
    even_numbers_lst = []
    for i in args:
        try:
            if i % 2 == 0:
                even_numbers_lst.append(i)

        except TypeError:
            continue 
        
    return even_numbers_lst


def lst(even_numbers_lst):
    count = 1
    for i in even_numbers_lst:
        print(f'{count} - {i}')
        count += 1

lst(show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12))