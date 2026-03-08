from data_files.loan_agreement_extraction import interest_rate, loan_term
import seaborn as sns

def create_chart(price, down_payment):
    monthly_payments = list()
    actal_price = price - down_payment
    their_interest_rate = (interest_rate / 100) + 1
    actual_price = actual_price * their_interest_rate
    monthly_payment = actual_price / loan_term
    for i in range(1, loan_term - 1):
        monthly_payments[i] = monthly_payment * i
    
    months = list()
    for i in range(1, loan_term - 1):
        months[i] = i

    sns.lineplot(monthly_payments, x="months", y="monthly_payments", hue="monthly_payments")

