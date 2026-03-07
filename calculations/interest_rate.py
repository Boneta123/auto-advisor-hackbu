def get_interest_rates(credit, age, duration, isNew) -> tuple:
    match isNew:
        case True:
            if credit > 780:
                base = 4.66
            elif credit <= 780 and credit > 660:
                base = 6.27
            elif credit <= 660 and credit > 600:
                base = 9.57
            elif credit <= 600 and credit > 500:
                base = 13.17
            elif credit <= 500 and credit > 300:
                base = 16.01
            else:
                #credit score is invalid
                return (0, 0)
        case False:
            if credit <= 850 and credit > 780:
                base = 7.70
            elif credit <= 780 and credit > 660:
                base = 9.98
            elif credit <= 660 and credit > 600:
                base = 14.49
            elif credit <= 600 and credit > 500:
                base = 19.42
            elif credit <= 500 and credit > 300:
                base = 21.85
            else:
                #credit score is invalid
                return (0, 0)
    
    if duration <= 48:
        low = base - 1
        high = base + 1
    elif duration == 60:
        low = base - 1
        high = base + 2
    elif duration == 72:
        low = base - 1
        high = base + 3
    elif duration >= 84:
        low = base - 0.5
        high = base + 3.5

    if age < 21:
        low += 1
        high += 1
    elif age < 25:
        low += 0.5
        high += 0.5

    return (low, high)

