from flask import request
from flask_restful import Resource
from db import db
from models import *

class CategoryAll(Resource):
    def get(self):
        categories = Category.query.all()
        categories_ordered = sorted(categories, key = lambda category: category.position)
        return [category.serialize() for category in categories_ordered if category.is_deleted == False]
    
class CategoryOne(Resource):
    def get(self):
        category = Category.query.get(request.args.get('category_id'))
        if category is None:
           return {"message" : "dishes not found"}, 404
        return [dish.serialize() for dish in category.dishes if dish.is_deleted == False]
