from sqlalchemy.orm import sessionmaker
from models import Book, Shop, Sale, engine, Stock, Publisher

Session = sessionmaker(bind=engine)
session = Session()


def get_shops(user):
    sample = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale,
    ).select_from(Shop).\
        join(Stock, Stock.id_shop == Shop.id).\
        join(Book, Book.id == Stock.id_book).\
        join(Publisher, Publisher.id == Book.id_publisher).\
        join(Sale, Sale.id == Book.id)

    if user.isdigit():
        sample1 = sample.filter(Publisher.id == int(user)).all()
        for nameb, names, saleb, dateb in sample1:
            print(f"{nameb: <40} | {names: <10} | {saleb: <8} | {dateb.strftime('%d-%m-%Y')}")
    else:
        sample2 = sample.filter(Publisher.name == user).all()
        for nameb, names, saleb, dateb in sample2:
            print(f"{nameb: <40} | {names: <10} | {saleb: <8} | {dateb.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    user = input("Введите имя или ID публициста: ")
    get_shops(user)

session.close()
