
import json
from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale, engine

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)


model_map = {
    'publisher': Publisher,
    'shop': Shop,
    'book': Book,
    'stock': Stock,
    'sale': Sale,
}

for record in data:
    model_name = record.get('model')
    model = model_map.get(model_name)

    if model:
        session.add(model(id=record.get('pk'), **record.get('fields')))

session.commit()


session.close()