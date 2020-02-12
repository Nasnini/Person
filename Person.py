#Main class
class Person:
    #Constructor
    def __init__(self,name,age,gender,interests=[]):

        self.name = name
        self.age = int(age) #Only an integer value is parsed for age
        self.gender = gender
        self.interests = interests

    #Hello function
    def hello(self):
        interests = ', '.join(self.interests)
        print(f'Hello, my name is {self.name} and I am {self.age} years old. My interests are {interests}.')
        return self.hello

#Values to be parse in the attributes
person = Person('Ryan','30','male',{'being a hardarse', 'agile', 'and ssd hard drives'})
#Print the hello functions
person.hello()
