import mysql.connector
from os import getenv
import pandas as pd

#database
db = mysql.connector.connect(
    host = "34.89.10.250",
    user = "root",
    password = getenv('db_password'),
    database = "books"
)

cursor = db.cursor()

# with open('books.csv', 'r') as books:
#     for line in books:
#         entries = line.strip().split(',')
#         isbn, title, author, published, pages = entries[0], entries[1], entries[2], entries[3], int(entries[4])
#         cursor.execute(f"INSERT INTO books VALUES ('{isbn}', '{title}', '{author}', '{published}', {pages});")
#         db.commit()

def search(search_by, term):
    if search_by not in ['pub_date', 'pages']:
        cursor.execute(f"SELECT * FROM books WHERE {search_by} LIKE '%{term}%'")
    else:
        cursor.execute(f"SELECT * FROM books WHERE {search_by} = {term}")

# while True:
#     search_by = input("What do you want to search by? ")
#     search_term = input("Enter search term: ")
#     search(search_by, search_term)
#     print(cursor.fetchall())

cursor.execute("SELECT * FROM books;")
data = cursor.fetchall()
fields = ['isbn', 'title','author', 'pub_date', 'pages']
pd_data = {fields[i]:[record[i] for record in data] for i in range(len(fields))}
df = pd.DataFrame(pd_data)
print(df)