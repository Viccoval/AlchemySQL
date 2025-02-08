import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "Publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Shop(Base):
    __tablename__ = "Shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Book(Base):
    __tablename__ = "Book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), nullable=False)

    book = relationship(Publisher, backref="books")

class Stock(Base):
    __tablename__ = "Stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Book, backref="stocks")
    stock1 = relationship(Shop, backref="stocks")

class Sale(Base):
    __tablename__ = "Sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL(10, 2), nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), nullable=False)
    date_sale = sq.Column(sq.DATE, nullable=False)
    count = sq.Column(sq. Integer, nullable=False)

    sale = relationship(Stock, backref="sales")


DSN = "postgresql://postgres:1995@localhost:5432/netology_bd"
engine = sqlalchemy.create_engine(DSN)
Base.metadata.create_all(engine)

