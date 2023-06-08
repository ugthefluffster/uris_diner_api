# Uri's Diner API

A Flask backend server for [uris-diner-digital-menu](https://github.com/ugthefluffster/uris-diner-digital-menu). Connects to the same PostgreSQL database as [uris_diner](https://github.com/ugthefluffster/uris_diner) website. Provides a simple restful API in JSON. 

## Frameworks and capabilities:

- Built using Flask and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- ORM provided by [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/), connects to a PostgreSQL database on Azure

## Making queries:  
Fetching a list of all categories
> /categories

```json
[
  {
    "id": <int:category.id>,
    "name": <str:category.name>,
    "image_src": <str:url to image>,
  }
]

```
Fetching a list of all the dishes of a single category
> /dishes?category_id=\<int>

```json
[
  {
    "id": <int:dish.id>,
    "name": <str:dish.name>,
    "price": <str:dish.price>,
    "image_src": <str:url to image>,
    "is_gluten_free": <bool:dish.is_gluten_free>,
    "is_vegeterian": <bool:self.is_vegeterian>,
    "description": <str:self.description>
  }
]
```
