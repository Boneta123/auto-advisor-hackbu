from flask import Flask, render_template

from data_files import loan_agreement_extraction

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/analyze')
def analyze ():
    make = loan_agreement_extraction.make
    model = loan_agreement_extraction.model
    year = loan_agreement_extraction.year
    loan_term = loan_agreement_extraction.loan_term
    interest_rate = loan_agreement_extraction.loan_term
    return render_template('index.html', make=make, model=model, year=year, loan_term=loan_term, interest_rate=interest_rate)

if __name__ == "__main__":
    app.run(port=8000, debug=True)