class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print('{} {}'.format(self.name, self.age))

def getUser():
    name = input('Name: ')
    age = input('Age: ') 
    usr= User(name, age)
    return usr



def main():
    usr = getUser()
    usr.show()


if __name__ == '__main__':
    main()