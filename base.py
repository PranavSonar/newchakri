from flask import Flask, render_template, url_for
from levels import levels
from levels import levels2
from datetime import date, timedelta
import datetime
import json
from dateutil.relativedelta import relativedelta, FR

app = Flask(__name__)

@app.route('/daily')
def daily():
    end_date = datetime.date.today()
    start_date = end_date - timedelta(days=7)

    nifty_50_daily = levels.Daily("NIFTY 50", start_date, end_date)
    nifty_50_daily.get_index_price_history()

    bank_nifty_daily = levels.Daily("BANKNIFTY", start_date, end_date)
    bank_nifty_daily.get_index_price_history() 

    data = {}
    data['css'] = url_for('static', filename='css/bootstrap.min.css')
    data['js'] = url_for('static', filename='js/bootstrap.min.js')

    data['bank_nifty_daily'] = bank_nifty_daily.angles()
    data['nifty_50_daily'] = nifty_50_daily.angles()
    
    return render_template('home.html', data = data)

# @app.route('/weekly')
def weekly():
    end_date = datetime.datetime.today() + relativedelta(weekday=FR(-1))
    start_date = end_date - timedelta(days=20)

    nifty_50_weekly = levels.Weekly("NIFTY 50", start_date, end_date)
    nifty_50_weekly.get_index_price_history()

    bank_nifty_daily = levels.Weekly("BANKNIFTY", start_date, end_date)
    bank_nifty_daily.get_index_price_history() 

    print(nifty_50_weekly.angles())

def new_daily():
    end_date = datetime.datetime.now()
    start_date = end_date - timedelta(days=7)
    nifty_50_daily = levels2.Daily("NIFTY 50", start_date, end_date)
    nifty_50_daily.main()

if __name__ == "__main__":
    new_daily()