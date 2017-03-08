import sqlite3
import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from flask import Flask, render_template

from data import get_rates, get_lowest_rate, add_data

app = Flask(__name__)


@app.route('/')
def index():
    rates = get_rates()
    lowest = get_lowest_rate(rates)
    historical = get_historical_data()
    chart = create_chart(historical)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(chart)

    return render_template(
        'index.html',
        points=len(historical),
        rates=lowest,
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )


def get_historical_data():
    all_data = []
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM rates""")
        rows = c.fetchall()
        for value in rows:
            all_data.append({
                'currency': value[0],
                'price': value[1],
                'time': value[2]
            })
        return all_data


def create_chart(data):
    data.sort(key=lambda d: d['time'])
    # create figure
    p = figure(
        x_axis_label='time',
        y_axis_label='price',
        x_axis_type="datetime",
        width=1000,
        height=500
    )
    # get x and y axis data
    curr_1_x = []
    curr_1_y = []
    curr_2_x = []
    curr_2_y = []
    curr_3_x = []
    curr_3_y = []
    for value in data:
        time = datetime.datetime.strptime(
            value['time'], '%Y-%m-%d %H:%M:%S')
        if value['currency'] == 'bitstamp':
            curr_1_x.append(time)
            curr_1_y.append(value['price'])
        if value['currency'] == 'kraken':
            curr_2_x.append(time)
            curr_2_y.append(value['price'])
        if value['currency'] == 'bittrex':
            curr_3_x.append(time)
            curr_3_y.append(value['price'])

    p.line(curr_1_x, curr_1_y, color='red', legend='bitstamp', line_width=2)
    p.line(curr_2_x, curr_2_y, color='green', legend='kraken', line_width=2)
    p.line(curr_3_x, curr_3_y, color='black', legend='bittrex', line_width=2)
    p.legend.location = 'bottom_left'

    return p


if __name__ == '__main__':
    app.run(debug=True)
