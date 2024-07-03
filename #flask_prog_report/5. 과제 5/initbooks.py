import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#database_setup.py file에서 각 class import
from database_setup_book import BookStore, Base, BookItem

engine = create_engine('mysql+pymysql://root:root@localhost/bookstore')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#make bookstore
store1=BookStore(name="ssu")

session.add(store1)
session.commit()

book1=BookItem(name="hi",price="$10",bookstore=store1)

session.add(book1)
session.commit()

book2=BookItem(name="world",price="$5",bookstore=store1)

session.add(book2)
session.commit()

#make again

store2=BookStore(name="nav")

session.add(store2)
session.commit()

book1=BookItem(name="python",price="$12",bookstore=store2)

session.add(book1)
session.commit()

book2=BookItem(name="C++",price="$15",bookstore=store2)

session.add(book2)
session.commit()

book3=BookItem(name="java",price="$14",bookstore=store2)

session.add(book3)
session.commit()

print("books are added")