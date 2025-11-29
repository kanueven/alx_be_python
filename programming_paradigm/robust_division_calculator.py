def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors:
    - Division by zero
    - Non-numeric input
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return " Error: Please enter numeric values only"
    
    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    else:
        return f"The result of the division is {result}"