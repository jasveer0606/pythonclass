#Sqlite
import sqlite3

conn = sqlite3.connect('example.db')
curs = conn.cursor()

#TABLES
books={'bookid':'number(3)','titleid':'number(3) primary key','location':'text','genre':'text',0:'books'}
titles={'titleid':'number(3)','title':'text','isbn':'text','pubid':'text',0:'titles'}
publishers={'pubid':'text','name':'text','street':'text','zip':'text',0:'publishers'}
zipcodes={'zip':'text','city':'text','state':'text','zipcode':'text',0:'zipcodes'}
authortitles={'authortitleid':'number(3)','authorid':'number(3)','titleid':'number(3)',0:'authortitles'}
authors={'authorid':'number(3)','first':'text','middle':'text','last':'text',0:'authors'}

for table in [books,titles,publishers,zipcodes,authortitles,authors]:
    curs.execute("CREATE TABLE "+table[0]+"("+','.join(["{} {}".format(i,table[i]) for i in table if i is not 0])+");")

#Insert
vals = [(100,100,'Chennai','Action'),
        (101,101,'Mumbai','Thriller'),
        (102,102,'Delhi','Horror'),
        (103,103,'Chennai','Action')]
curs.executemany('INSERT INTO books VALUES (?,?,?,?);',vals)
print '4 rows added.\n'

#Select
print 'Running Query: SELECT * FROM books;'
print '\n'.join([str(res) for res in curs.execute("SELECT * FROM books;")])
