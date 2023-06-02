from db import db
from config import STORAGE_URL

def get_image_src(self):
    if self.image_file:
        return f'{STORAGE_URL}/{self.image_file}'
    else:
        return self.image_Url

class Category(db.Model):
    __tablename__ = 'main_category'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    is_deleted = db.Column(db.Boolean)
    image_Url = db.Column(db.Text)
    image_file = db.Column(db.Text)
    position = db.Column(db.Integer)
    dishes = db.relationship('Dish', backref='category')

    @property
    def image_src(self):
        return get_image_src(self)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_src": self.image_src,
        }

class Dish(db.Model):
    __tablename__ = 'main_dish'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    description = db.Column(db.String(300))
    is_gluten_free = db.Column(db.Boolean)
    is_vegeterian = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)
    image_Url = db.Column(db.Text)
    image_file = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('main_category.id'), nullable = False)

    @property
    def image_src(self):
        return get_image_src(self)

    def serialize(self):
        print(type(self.price))
        return {
            "id": self.id,
            "name": self.name,
            "price": str(self.price),
            "image_src": self.image_src,
            "is_gluten_free": self.is_gluten_free,
            "is_vegeterian": self.is_vegeterian,
            "description": self.description
        }
