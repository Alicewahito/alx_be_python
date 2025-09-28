# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters
    ----------
    num1 : float
        First operand.
    num2 : float
        Second operand.
    operation : str
        One of: 'add', 'subtract', 'multiply', 'divide' (case-insensitive).

    Returns
    -------
    float or str
        The numeric result for successful operations, or a string error message
        for division-by-zero or invalid operation.
        Division-by-zero returns the exact string: "Cannot divide by zero".
        Invalid operation returns: "Invalid operation".
    """
    # Normalize operation string so input like " Add " or "DIVIDE" work
    if not isinstance(operation, str):
        return "Invalid operation"

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        # handle division by zero explicitly
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
