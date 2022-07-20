#create table

import sqlite3
#connecting to database
db = sqlite3.connect('bookstore.db')
#creating a cursor object
cursor = db.cursor()
#code to create the table and it's fields
cursor.execute(''' CREATE TABLE IF NOT EXISTS books(id INTEGER, Title TEXT,Author TEXT, QTY INTEGER) ''')
#saving the table books
db.commit

#records to be entered into the table
id1 = 3001
Title1 = '''A Tale of Two
            Cities'''
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = '''Harry Potter and
            the
            Philosopher's
            Stone'''
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003
Title3 = '''The Lion, the
            Witch and the
            Wardrobe'''
Author3 = 'C. S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = '''The Lord of the
            Rings'''
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005
Title5 = '''Alice in
            Wonderland'''
Author5 = 'Lewis Carroll'
Qty5 = 12

#code to enter all the above records into the table
books = [(id1,Title1,Author1,Qty1), (id2,Title2,Author2,Qty2), (id3,Title3,Author3,Qty3), (id4,Title4,Author4,Qty4), (id5,Title5,Author5,Qty5)] 
cursor.executemany(''' INSERT INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)''', books)
print(books)
db.commit()
print('\n')

print('**********************************************************************************')
# import mysql.connector as code
# beg = code.connect(database = 'Library')

#creating a function to add books
def addbook():
    a = input('Enter the title of the book: \n-')
    b = input('Enter the author of the book: \n-')
    c = input('Enter the qty of the book: \n-')
    d = input('Enter the id of the book \n-')
    facts = (a, b, c, d)
    sql = 'insert into books values(%s, %s, %s, %s)'
    # e = db.cursor()
    cursor.execute(sql, facts)
    db.commit()
    print('********************************************************************************')
    print('Successful')
    main()


#creating a function to update books
def upbook():
    a = input('Enter the id of the book: \n-')
    b = 'update from book where id = %s'
    facts = (a,)
    c = db.cursor()
    c.execute(b,facts)
    db.commit
    main

#creating a function to delete books
def dbook():
    ab = input('Enter the id of the book: \n-')
    bc = 'delete from book where id = %s'
    facts = (ab,)
    c = db.cursor()
    c.execute(bc, facts)
    db.commit()
    main()

#creating a function to search books
def seabook():
    q = input('What is the name of the book that you want to search: ').casefold()
    my_sql = 'SELECT * FROM table book'
    # cursor.execute(my_sql)
    # colName = cursor.description[colNum][0]
    # sql_search = 'SELECT * FROM BOOKS WHERE id  = %s'
    # place = []
    # for field in cursor.description:
    #     place.append(field[0])



#creating the main menu
def main():

    print('''
            1. Enter book
            2. Update book
            3. Delete book
            4. Search books
            ''')
option = input('''
1. Enter book
2. Update book
3. Delete book
4. Search books

Choose your option: ''')
print('*******************************************************************')
if option == '1':
    addbook()

elif option == '2':
    upbook()

elif option == '3':
    dbook()

elif option == '4':
    seabook()

else:
    print('Incorrect option..... please try again later!!!')



