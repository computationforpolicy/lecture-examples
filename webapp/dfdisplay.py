from flask import Flask
from flask import render_template
import pandas as pd
app = Flask(__name__)


import config


df = pd.read_csv(config.file_to_display)


@app.route('/')
def load_dataframe():
    cols = list(df.columns)
    return render_template('dataframe.html', data=df.to_dict(), cols=cols, nrows=len(df))


@app.errorhandler(404)
def not_found(error):
    return '404!!!!'


if __name__ == '__main__':
    app.run()
