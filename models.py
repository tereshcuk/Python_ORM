import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import sqlalchemy


Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=250), unique=True)

    
class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=250), unique=True)


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=250), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey(Publisher.id), nullable=False) 
        
    publisher = relationship("Publisher", backref="book")  
    
    
class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey(Book.id), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey(Shop.id), nullable=False)
    count = sq.Column(sq.Integer)
     
    book = relationship("Book", backref="stock")
    shop = relationship("Shop", backref="stock")
  
    
class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric,)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey(Stock.id), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship("Stock", backref="sale")  
    
    
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)  
    
  
     
    