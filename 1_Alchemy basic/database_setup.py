import sys
import pymysql  # db connector(software)
# sqlalchemy: flask framework 에서 사용하는 ORM library 이름
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


# declarative_base() : Table 생성을 위한 부모 class인 Base 생성하는 함수
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    # restaurant _id 값은 외부에서 받는게 아니라  restaurant 객체를 통해 간접적으로 가져옴
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


##### insert at end of file #####

engine = create_engine('mysql+pymysql://root:root@localhost/restaurant')
# engine = create_engine('mysql+pymysql://root:root@localhost')
# engine.execute("DROP DATABASE IF EXISTS restaurant")
# engine.execute("CREATE DATABASE restaurant default CHARACTER SET UTF8")
# engine.execute("USE restaurant")
Base.metadata.create_all(engine)
