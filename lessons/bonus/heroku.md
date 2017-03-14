# Heroku

In this session, we will deploy out app to Heroku

## Objectives

By the end of this lesson, you should be able to:

1. Deploy an app to Heroku running with Postgres

## Heroku Setup

1. Create a [Heroku account](https://signup.heroku.com) (if necessary)
1. Download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  and then run `heroku login` (if necessary)

## Project Setup

Did you finish the [SQLAlchemy lesson](sqlalchemy.md)?

1. If yes - navigate to your project directory and activate the virtualenv.
1. If no -

    Clone the app:

    ```sh
    $ git clone https://github.com/realpython/flask-bitcoin-example --branch v2 --single-branch -b master
    ```

    Create and activate a virtualenv and then install the dependencies:

    ```sh
    $ python3.6 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

Next, we need to update the app config in *app.py* to use either an environment variable, which will be set by Heroku, or our local SQLite database:

```python
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')
DATABSE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + DATABASE_PATH)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    return 'Hello, world'


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


port = int(os.environ.get('PORT', 8080))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
```

This also updates how the port number is set.

Then install [psycopg2](http://initd.org/psycopg/) so that our app can communicate with Postgres along with [gunicorn](http://gunicorn.org/), a web server. Let's also update all dependencies. Update *requirements.txt*:

```
click==6.7
Flask==0.12
Flask-SQLAlchemy==2.2
gunicorn==19.7.0
itsdangerous==0.24
Jinja2==2.9.5
MarkupSafe==1.0
psycopg2==2.7.1
requests==2.13.0
schedule==0.4.2
SQLAlchemy==1.1.6
Werkzeug==0.12
```

```sh
$ pip install -r requirements.txt
```

Then update the schedule to fire every hour:

```python
import schedule
import time

from data import get_data, add_data


def test():
    data = get_data()
    if data:
        add_data(data)
        print('got data')


schedule.every().hour.do(test)

while True:
    schedule.run_pending()
    time.sleep(1)
```

Finally, add a *runtime.txt* file to the project root and add the text `python-3.6.0` to it. This will inform Heroku that we are using the Python 3.6 runtime.

## Heroku Deploy

Commit your code to Git, and then create a new app on Heroku:

```sh
$ heroku create
```

 Push your code to Heroku:

```sh
$ git push heroku master
```

Add a database:

```sh
$ heroku addons:create heroku-postgresql:hobby-dev
```

Create the DB schema:

```sh
$ heroku run python create_db.py
```

Then restart the app:

```sh
$ heroku restart
```
