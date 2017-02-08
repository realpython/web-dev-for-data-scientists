# Lesson 2: Flask Quick Start

In this second session, we'll dive into Flask, a powerful Python web framework...

## Objectives

By the end of this lesson, you should be able to answer the following questions:

1. What is Flask?
1. Why are we using Flask?
1. What is server-side templating?

You should also be able to:

1. Set up a Flask app that-
  - Uses dynamic URLs.
  - Handles requests via route handlers.
  - Responds with both JSON and HTML via Jinja templates.
  - Persists data with SQLite.

## Welcome

Slides: `npm run day2`

## Flask

<img src="../slides/images/flask.png" width="40%">

### What?

Flask is a microframework written in Python.

### Why?

Why are we using Flask over other Python web frameworks like Django?

1. Flask is considered more Pythonic than Django since, in most cases, it's more explicit. It's also much lighter than Django so you can quickly get an app up and running.
1. Less magic.

Flask is a solid framework:

1. It scales well.
1. Strong community.
1. You can learn A LOT from just reading the source code since it's so well documented.
1. It's perfect for microservices and RESTful APIs.
1. It's the right tool for *some* jobs.

## Quick Start

Create a project directory:

```sh
$ mkdir flask-hello-world
$ cd flask-hello-world
```

Create and activate a virtualenv:

```sh
$ python3.6 -m venv env
$ source env/bin/activate
```

Install Flask v[0.12](https://pypi.python.org/pypi/Flask/0.12):

```sh
(env)$ pip install Flask==0.12
(env)$ pip freeze > requirements.txt
```

Add an *app.py* file:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

> **NOTE**: Want to know more about the Flask instance, `Flask(__name__)`? Check out the official [docs](http://flask.pocoo.org/docs/0.12/api/#application-object).

Run:

```sh
(env)$ python app.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger pin code: 292-049-281
```

Navigate to [http://localhost:5000/](http://localhost:5000/) in your browser, and you should see `Hello, World!` staring back at you.

### What's happening?

Review *Flask: Quick Start* in **Real Python Course 2**.

## Flask Calculator

Let's build a basic calculator together...

1. Create a new project.
1. Before you write any code, make sure everything is wired up correctly and get a sanity check. Why is this important?
1. Set up the one route:
  - `/calc/:operator/:num1/:num2`
1. Respond with JSON:

  ```json
  {
    "operator": "add",
    "num1": "9",
    "num2": "3",
    "solution": "12"
  }
  ```

## Templating

The view is handled/managed with server-side templates. Like the name suggests, server-side templates are generated on the server. So, when a user hits a route, the server responds with the full HTML page, which is then rendered in the browser.

We'll be using [Jinja2](http://jinja.pocoo.org/docs/2.9/), which Flask already depends on, for our server-side templating engine. With it, you can add Python-like variables and logic (conditionals, loops) to your templates.

### Getting Started

Add a "templates" folder to your calculator project, and then add an *index.html* file to that folder:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Flask Calculator</title>
  </head>
  <body>
    <!-- add content -->
  </body>
</html>
```

Update your route handlers to render a template rather than JSON:

```python
data = { 'num1': '9', 'num2': '3', 'operator': 'add', 'solution': '12' }
return render_template('index.html', data=data)
```

You can access variables in your template like so: `{{data.num1}}`. Update your template to display:

```
You entered 9 and 3. You chose to add. The solution is 12.
```

Your turn!

- Add a conditional to check if the solution exists. If it exists, then display the above text. If it doesn't exist, display the text - "Nothing to calculate at this time."
  - Hint:

    ```html
    {% if true %}
      <p>foo</p>
    {% else %}
      <p>bar</p>
    {% endif %}
    ```

- Set up [template inheritance](http://jinja.pocoo.org/docs/2.9/templates/#template-inheritance) to create a base and child template.

> **NOTE**: Review [Primer on Jinja Templating](https://realpython.com/blog/python/primer-on-jinja-templating/) for more on Jina and Templating.

## SQL

Right now we are not saving any of our precious calculations. Let's set up [SQLite](https://sqlite.org/) to persist our data.

Add a new file called *sql.py* to the project root:

```python
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('calc.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE calculations
             (num1 INTEGER, num2 INTEGER, operator TEXT, solution REAL)
              """)

    # insert dummy data into the table
    c.execute('INSERT INTO calculations VALUES(9, 3, "add", 12)')
    c.execute('INSERT INTO calculations VALUES(9, 3, "sub", 6)')
    c.execute('INSERT INTO calculations VALUES(9, 3, "mult", 27)')
    c.execute('INSERT INTO calculations VALUES(9, 3, "div", 3)')
```

Add a new route handler (`/calc`) that displays all calculations. Set up the base structure:

```python
@app.route('/calc')
def calc():
    return 'sanity check!'
```

Get the data out of the database:

```python
@app.route('/calc')
def calc():
    with sqlite3.connect('calc.db') as connection:
        # create cursor
        c = connection.cursor()
        # exectute SQL statement
        c.execute("""SELECT * FROM calculations""")
        rows = c.fetchall()
        print(rows)
```

What kind of data structure can we use to store the data to easily send it to a template to render? Update the code.

```python
@app.route('/calc')
def calc():
    with sqlite3.connect('calc.db') as connection:
        # create cursor
        c = connection.cursor()
        # exectute SQL statement
        c.execute("""SELECT * FROM calculations""")
        rows = c.fetchall()
        print(rows)
        # pass data to the view
        return render_template('calc.html', rows=rows)
```

Instead of a template, why not try to just send it back as JSON:

```json
[
  {
    "operator": "add",
    "num1": "9",
    "num2": "3",
    "solution": "12"
  },
  {
    "operator": "sub",
    "num1": "9",
    "num2": "3",
    "solution": "6"
  },
  {
    "operator": "mult",
    "num1": "9",
    "num2": "3",
    "solution": "27"
  },
  {
    "operator": "div",
    "num1": "9",
    "num2": "3",
    "solution": "3"
  }
]
```

Once done, your app should have the following routes:

- `/calc/:operator/:num1/:num2`
- `/calc/`

## Homework

1. Review the Flask lesson from the beginning. See where you get stuck. You should see things a bit differently this time around. For example, if you were stuck on the Python syntax before, it's always good to review after you have a better grasp on the syntax so that you take in the deeper concepts.
1. Complete [Python: Visualization with Bokeh](https://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/)
1. Complete the [Bokeh Quickstart](http://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart)
1. Complete the [Flask Bokeh Basics](https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md) tutorial
1. (Optional) Want to learn HTML and CSS? Go through an [Introduction to HTML and CSS](https://github.com/mjhea0/thinkful-html).
1. (Optional) Want to learn more SQL? Review *Interlude: Database Programming* in **Real Python Course 2**.
