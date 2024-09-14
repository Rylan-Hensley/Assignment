import sqlite3
import sqlalchemy as sa
from sqlalchemy.sql import text

meta = sa.MetaData()
books = sa.Table('books', meta, 
                 sa.Column('title', sa.String, primary_key=True),
                 sa.Column('author', sa.String),
                 sa.Column('year', sa.Integer)
                 )

conn = sa.create_engine('sqlite:///books.db')
meta.create_all(conn)

state = conn.connect()

data = (
    {'Title_1', 'Author_1', 1978},
    {'Title_2', 'Author_2', 1999},
    {'Title_3', 'Author_3', 2015},
)

#statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

state.execute(text("INSERT INTO books(title, author, year) VALUES('Big World', 'Author_1', 1978)"))
state.execute(text("INSERT INTO books(title, author, year) VALUES('Little World', 'Author_2', 1999)"))
state.execute(text("INSERT INTO books(title, author, year) VALUES('Normal World', 'Author_3', 2015)"))

#result = conn.execute(books.select())

#rows = result.fetchall()
#print(rows)

rs = state.execute(text('SELECT * FROM books ORDER BY title ASC'))
for row in rs:
    print(row)

