import pytesseract
import re
from PIL import Image

import pytesseract
from PIL import Image, ImageFilter

def clean_text(value):
    return re.sub(r'[^A-Za-z0-9 \-]', '', value) if value else None

def extract_loan_info (file_name):
    img = Image.open(file_name)

    img = img.convert("L")  # grayscale
    img = img.filter(ImageFilter.SHARPEN)

    text = pytesseract.image_to_string(img)

    make_match = re.search(r"Make.*?:?\s*(\w+)", text)
    model_match = re.search(r"Mode.*?:?:\s*(\w+)", text)
    year_match = re.search(r"Yea.*?:?\s*(\d{4})", text)
    interest_match = re.search(r"Annual Interest.*?:?\s*([\d\.]+%?)", text)
    loan_match = re.search(r"Loan\s+Term.*?:?\s*([^\n]+)", text)

    make = make_match.group(1) if make_match else None
    model = model_match.group(1) if model_match else None
    year = year_match.group(1) if year_match else None
    their_interest_rate = interest_match.group(1) if interest_match else None
    loan_term = loan_match.group(1) if loan_match else None

    make = clean_text(make)
    model = clean_text(model)
    year = clean_text(year)
    their_interest_rate = clean_text(their_interest_rate)
    loan_term = clean_text(loan_term)