from flask import Flask, render_template

from data_files import data_extraction

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/analyze')
def analyze ():
    make = data_extraction.make
    model = data_extraction.model
    year = data_extraction.year
    loan_term = data_extraction.loan_term
    interest_rate = data_extraction.loan_term
    return render_template('index.html', make=make, model=model, year=year, loan_term=loan_term, interest_rate=interest_rate)

if __name__ == "__main__":
    app.run(port=8000, debug=True)