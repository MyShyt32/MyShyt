import os
import sqlite3

wd = os.getcwd()
dw = '/game'
db = 'database.db'
gamePath = wd + dw
dbPath = gamePath + '/' + db

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.age = password
    def show(self):
        print('{} {} {}'.format(self.id, self.name, self.age))

def createUser():
    id =  None
    name = input('Create username: ')
    password = input('Create password: ') 
    usr= User(id, name, password)
    return usr

def loadUser():
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    cur.execute("SELECT NAME FROM USERS")
    if len(cur.fetchall()) == 0:
        createUser()
    else:
        for row in cur.fetchall():
            users = []
            users.append(row)

def pickUser(users):
    for user in users:
        

def createDb():
    os.mkdir(gamePath)
    con = sqlite3.connect(dbPath)
    con.execute("""CREATE TABLE USERS 
                (ID INT PRIMARY KEY, 
                NAME TEXT UNIQUE NOT NULL, 
                PASSWORD TEXT NOT NULL)""")
    con.commit()
    con.close

def main():
    if os.path.exists(dbPath):
        loadUser()
    else:
        createDb()
        main()

if __name__ == '__main__':
    main()