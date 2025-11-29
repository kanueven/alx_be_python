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
        return "Error: Please enter numeric values only."
    
    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of the division is {result}"
