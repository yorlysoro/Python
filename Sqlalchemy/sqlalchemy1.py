from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

engine = create_engine('sqlite:///library.db', echo=True)
metadata = MetaData()

authors_table = Table('authors', metadata,
Column('id', Integer, primary_key=True), Column('name', String))

books_table = Table('books', metadata,
Column('id', Integer, primary_key=True),
Column('title', String),
Column('description', String),
Column('author_id', ForeignKey('authors.id')))
metadata.create_all(engine)

insert_stmt = authors_table.insert(bind=engine)
compiled_stmt = insert_stmt.compile()

insert_stmt.execute(name='Alexandre Dumas')
insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}])

metadata.bind = engine
select_stmt = authors_table.select(authors_table.c.id==2)
result = select_stmt.execute()
print(result.fetchall())

del_stmt = authors_table.delete()
del_stmt.execute(whereclause=text("name='Mr Y'"))
del_stmt.execute()
