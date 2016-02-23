from flask import Flask
from flask import render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def load_dataframe():
    filename = '../Current_Employee_Names__Salaries__and_Position_Titles.csv'
    df = pd.read_csv(filename)
    return render_template('unfiltered.html', data=df.to_html())


@app.errorhandler(404)
def not_found(error):
    return '404!!!!'


if __name__ == '__main__':
    app.run(debug=True)
