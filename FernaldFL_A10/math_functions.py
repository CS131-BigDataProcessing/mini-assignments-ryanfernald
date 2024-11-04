#math funcitons

class IndeterminateFormError(Exception):
    """Custom exception for indeterminate forms."""
    pass

def power(x, y):
    """
    Calculate x raised to the power of y.

    Parameters:
    x (int or float): Base number.
    y (int or float): Exponent.

    Returns:
    int or float: x raised to the power of y.

    Raises:
    TypeError: If x or y is not a number.
    IndeterminateFormError: If x is 0 and y is 0.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    
    if x == 0 and y == 0:
        raise IndeterminateFormError("Indeterminate form: 0^0")
    
    return x ** y

def division(x, y):
    """
    Divide x by y.

    Parameters:
    x (int or float): Dividend.
    y (int or float): Divisor.

    Returns:
    int or float: Quotient of x divided by y.

    Raises:
    TypeError: If x or y is not a number.
    ValueError: If y is zero.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
