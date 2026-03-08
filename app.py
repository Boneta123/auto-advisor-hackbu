from flask import Flask, render_template, request

from data_files import loan_agreement_extraction

from calculations import interest_rate, price

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/analyze')
def analyze ():
    
    file_name = request.files["loan-agreement"]
    loan_agreement_extraction.extract_loan_info(file_name)

    make = loan_agreement_extraction.extract_loan_info(file_name).make
    model = loan_agreement_extraction.extract_loan_info(file_name).model
    year = loan_agreement_extraction.extract_loan_info(file_name).year
    loan_term = loan_agreement_extraction.extract_loan_info(file_name).loan_term
    their_interest_rate = loan_agreement_extraction.extract_loan_info(file_name).their_interest_rate

    credit = request.form["credit-score"]
    age = request.form["age"]
    isNew = request.form["isNew"]
    
    our_interest_rate = interest_rate.get_our_interest_rates(credit, age, loan_term, isNew)

    their_price = request.form["purchase-price"]
    market_value = price.get_market_value(year, make, model, "Average")
    
    return render_template('index.html', make=make, model=model, year=year, loan_term=loan_term, their_interest_rate=their_interest_rate, our_interest_rate=our_interest_rate, market_value=market_value)

if __name__ == "__main__":
    app.run(port=8000, debug=True)