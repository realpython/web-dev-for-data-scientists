# SQLAlchemy

In this session, we will refactor our app to use a powerful ORM called [SQLAlchemy](https://www.sqlalchemy.org/), via [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/), so that we can utilize Postgres.

## Objectives

By the end of this lesson, you should be able to:

1. Add Flask-SQLAlchemy to your app to interact with the database

## Getting Started

Clone the app:

```sh
$ git clone https://github.com/realpython/flask-bitcoin-example --branch v1 --single-branch -b master
```

Create and activate a virtualenv and then install the dependencies:

```sh
$ python3.6 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Right now your project structure looks like this:

```sh
├── Procfile
├── app.py
├── data.py
├── db.py
├── requirements.txt
├── run.sh
└── scheduler.py
```

## Adding SQLAlchemy

Install:

```sh
$ pip install Flask-SQLAlchemy==2.2
```

Update *app.py* to configure Flask-SQLAlchemy:

```python
import os
import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/data')
def data():
    all_data = []
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM currency""")
        rows = c.fetchall()
        for value in rows:
            all_data.append({
                'exchange': value[0],
                'price': value[1],
                'time': value[1]
            })
        return jsonify(all_data)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
```

We still need to update the route handlers. We'll come back to that once the database is set up.

Add a *models.py*:

```python
from datetime import datetime

from app import db


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String())
    price = db.Column(db.String())
    horah = db.Column(db.DateTime)

    def __init__(self, exchange, price, horah):
        self.exchange = exchange
        self.price = price
        if horah is None:
            horah = datetime.utcnow()
        self.horah = horah

    def __repr__(self):
        return '<Currency {}>'.format(self.exchange)
```

This sets up a `Model()` for the database. For more info, check out the [docs](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/).

Next, add a *create_db.py* file. This file is used to create the database:

```python
from app import db
from models import Currency


# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
```

Run `python create_db.py` to create the database. Make sure it looks right in the [SQLite Database Browser](http://sqlitebrowser.org/).

## Adding Data

Next, update the `add_data()` function in *data.py*:

```python
def add_data(bitDict):
    new_entry = Currency('bitstamp', bitDict['last'], None)
    db.session.add(new_entry)
    db.session.commit()
```

Make sure to add the imports:

```python
from app import db
from models import Currency
```

Install requests:

```sh
$ pip install requests
```

Then run `python data.py` to add data to the database. Again, ensure that the database looks right in the SQLite Database Browser.

## Refactoring Routes

Update `data()` in *app.py*:

```python
@app.route('/data')
def data():
    all_data = []
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.horah
        }
        all_data.append(obj)
    return jsonify(all_data)
```

Run the app via `python app.py` and navigate to [http://localhost:8080/data](http://localhost:8080/data) and you should see something similar to:

```json
[
  {
    "exchange": "bitstamp",
    "price": "1237.31",
    "time": "Tue, 14 Mar 2017 10:29:49 GMT"
  }
]
```

Kill the server. Add more data. Fire up the server and ensure that another object can be seen in that same route.
