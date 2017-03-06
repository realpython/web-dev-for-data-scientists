from flask import Flask, jsonify, render_template

from data import get_rates, get_lowest_rate, add_data

app = Flask(__name__)


@app.route('/')
def index():
    rates = get_rates()
    lowest = get_lowest_rate(rates)
    add_data(rates)
    return render_template('index.html', rates=lowest)


if __name__ == '__main__':
    app.run(debug=True)
