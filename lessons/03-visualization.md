# Lesson 3: Data Visualization

With the Flask basics behind us, this sessions focuses on how to visualize data with Flask and [Bokeh](http://bokeh.pydata.org/en/latest/), a Python interactive visualization library.

## Objectives

By the end of this lesson, you should be able to answer the following questions:

1. What is Bokeh?
1. Why would you want to use Bokeh over a different charting library?

You should also be able to:

1. Write a Python script to add data to SQLite
1. Embed a Bokeh chart into a Flask app

## Welcome

Slides: `npm run day3`

## Getting Started

Let's get a Flask app up and running!

### Setup

1. foo
1. bar

### SQLite

1. foo
1. bar

## Data Wrangling

### Normalize Data

1. Do we need to normalize the data?
1. If yes, when and how should we normalize it?

### Database Schema

1. foo

### Add Data to SQLite

1. foo

## Adding Bokeh

### What and Why?

1. What's Bokeh?
1. Why use Bokeh? Unlike matplotlib it's build for the web. Plus, it's all Python so you don't have to mess with JavaScript.

> **NOTE:** For more on Python data visualization tools, check out [Overview of Python Visualization Tools](http://pbpython.com/visualization-tools-1.html).

### Quick Start

#### Install:

```sh
$ pip install bokeh==0.12.4
```

#### Sanity check

Create a new route - `/sample`, and add the sample code for a [line chart](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#single-lines)

Add the imports:

```python
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
```

Update the route:

```python
@app.route('/sample')
def sample():

    # create the chart
    p = figure(plot_width=400, plot_height=400)

    # add a line renderer
    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # generate javascript and the actual chart via components()
    script, div = components(p)

    # render template
    return render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
```

### Add DB Data

1. Open database connection
1. Generate SQL query
1. Format data
1. Update Bokeh code

## Homework

1. Review the Visualization lesson from the beginning. See where you get stuck. You should see things a bit differently this time around.
1. Add a function called `drop_table()` to the *db.py* file that drops the `greenhouse` table. Make sure to call this function before you create the database table.
1. Add the air temperature data to the chart.
  - Drop the Database
  - Update the schema in *db.py*
  - Seed the database
  - Update the route handler
  - Update bokeh - convert to [multi-line](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#multiple-lines) chart
1. How do you make the graph smoother? More points? We need more data! Add all the data from "/data".
1. Practice making an external call to the [OMDb API](http://www.omdbapi.com/) within Flask. Start a new project. You can find sample code below. Just make sure to install the [requests](http://docs.python-requests.org/en/master/) library.

  ```python
  from flask import Flask
  import requests

  BASE = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'

  app = Flask(__name__)

  @app.route('/')
  def index():
        movie_name = 'star wars'
        url = BASE.format(movie_name)
        r = requests.get(url)
        json_response = r.json()
        print(json_response)
        return json_response


  if __name__ == '__main__':
      app.run(debug=True)
  ```

1. Think about where you'd like to make API calls to get data. [Socrata](https://dev.socrata.com/) is awesome!
