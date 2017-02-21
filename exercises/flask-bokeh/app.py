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
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []
    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM greenhouse""")
        rows = c.fetchall()
        for value in rows:
            date = datetime.datetime.utcfromtimestamp(
                value[0]).strftime('%Y-%m-%dT%H:%M:%SZ')
            if str(value[2]) == 'inside':
                inside_x.append(np.datetime64(date))
                inside_y.append(value[1])
            if str(value[2]) == 'outside':
                outside_x.append(np.datetime64(date))
                outside_y.append(value[1])
        x.append(inside_x)
        x.append(outside_x)
        y.append(inside_y)
        y.append(outside_y)

    p = figure(
        x_axis_label='time',
        y_axis_label='temp',
        x_axis_type="datetime",
        width=1000,
        height=600
    )
    p.multi_line(x, y, color=['firebrick', 'navy'], line_width=2)

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
