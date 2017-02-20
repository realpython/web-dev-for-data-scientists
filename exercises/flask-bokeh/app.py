import sqlite3
import datetime

import numpy as np

from flask import Flask, jsonify, render_template

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/data')
def data():
    all_data = []
    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM temperature""")
        rows = c.fetchall()
        for value in rows:
            all_data.append({
                'time': value[0],
                'temp': value[1]
            })
        return jsonify(all_data)


@app.route('/bokeh')
def bokeh():

    x = []
    y = []

    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM temperature""")
        rows = c.fetchall()
        for value in rows:
            date = datetime.datetime.utcfromtimestamp(value[0]).strftime(
                '%Y-%m-%dT%H:%M:%SZ')
            x.append(np.datetime64(date))
            y.append(value[1])

    p = figure(
        x_axis_label='x',
        y_axis_label='y',
        x_axis_type="datetime",
        width=1000,
        height=600
    )
    p.line(x, y, legend="Temp", line_width=2)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(p)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)


if __name__ == '__main__':
    app.run(debug=True)
