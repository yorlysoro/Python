#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqlalchemy2.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///library2.db')

class Author(Base):
	__tablename__ = 'authors'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return self.name
		
class Book(Base):
	__tablename__ = 'books'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	description = Column(String)
	author_id = Column(Integer, ForeignKey('authors.id'))
	author = relationship(Author, backref=backref('books', order_by=title))
	
	
	def __init__(self, title, description, author):
		self.title = title
		self.description = description
		self.author = author
		
	def __repr__(self):
		return self.title
		

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')

book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)

session.add(author_1)
session.add(author_2)
session.add(book_1)
session.add(book_2)
session.add(book_3)

session.commit()

book_3.description = u'The theory of evolution'
print(book_3 in session)

session.commit()

print(session.query(Book).order_by(Book.id))
print(session.query(Book).order_by(Book.id).all())

print(session.query(Book).filter(Book.title == 'The Selfish Gene').order_by(Book.id).all())
print(session.query(Book).filter(Book.title.like('The%')).order_by(Book.id).all())

query = session.query(Book).filter(Book.id == 9).order_by(Book.id)

print(query.count())
print(query.all())
print(query.first())
print(query.one())

query = session.query(Book).filter(Book.id == 1).order_by(Book.id)
book_1 = query.one()
print(book_1.description)
print(book_1.author.books)
