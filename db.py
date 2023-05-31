from tinydb import TinyDB, Query
from tinydb.database import Document

class DB:
    def __init__(self, path) -> None:
        self.ti = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.data = self.ti.table('data')

    def add_data(self, title, brend, model, price, img):
        self.data.insert({'title': title, 'brend': brend, 'model': model, 'price': price, 'img': img})