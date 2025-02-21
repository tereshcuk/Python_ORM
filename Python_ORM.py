
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
# import models
from models import create_tables, Publisher, Shop, Book, Stock, Sale



DSN = "postgresql://postgres:hua21WEI12_76@localhost:5432/publisher_bd"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


with open('fixtures/tests_data.json', 'r', encoding='utf-8') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

my_publisher=input('Введите id или имя автора: ')

if my_publisher.isnumeric():
    
    results = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
            .join(Publisher, Publisher.id == Book.id_publisher) \
            .join(Stock, Stock.id_book == Book.id) \
            .join(Shop, Shop.id == Stock.id_shop) \
            .join(Sale, Sale.id_stock == Stock.id) \
            .filter(Publisher.id == my_publisher).all()
    for book, shop, price, date in results:
        print(f'{book: <5} | {shop: <5} | {price: <5} | {date}')    
else:
    results = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
            .join(Publisher, Publisher.id == Book.id_publisher) \
            .join(Stock, Stock.id_book == Book.id) \
            .join(Shop, Shop.id == Stock.id_shop) \
            .join(Sale, Sale.id_stock == Stock.id) \
            .filter(Publisher.name == my_publisher).all()
    for book, shop, price, date in results:
            print(f'{book: <5} | {shop: <5} | {price: <5} | {date}')


session.close()