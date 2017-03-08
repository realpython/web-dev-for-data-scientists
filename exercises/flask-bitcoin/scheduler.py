import time
import schedule

from data import get_rates, add_data


def job():
    rates = get_rates()
    if rates:
        add_data(rates)
        print("I'm working...")


schedule.every(60).minutes.do(job)


def run():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()
