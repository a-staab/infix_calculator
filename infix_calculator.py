import re


def calculate(input_string):
    """Takes a string of space-separated integers and operators ("*", "/", "+",
    and "-") and computes the value of expression following normal
    order-of-operations associativity rules. Raises ArgumentError if invalid
    input is received.

    >>> calculate("4 + 4")
    8

    >>> calculate("2 * 2 + 4")
    8

    >>> calculate("6 / 3 - 2 * -4")
    10

    """

    try:
        inputs = input_string.split(" ")
    except:
        raise ArgumentError('Invalid input entered.')

    operators = set(["/", "*", "+", "-"])

    if not operators.intersection(inputs):
        raise ArgumentError('Invalid input entered.')

    try:
        while "/" in inputs:
            # handle_invalid(inputs)
            operator_location = inputs.index("/")
            subtotal = int(inputs[(operator_location - 1)]) / int(inputs[(operator_location + 1)])
            replace_with_subtotal(inputs, operator_location, subtotal)

        while "*" in inputs:
            # handle_invalid(inputs)
            operator_location = inputs.index("*")
            subtotal = int(inputs[(operator_location - 1)]) * int(inputs[(operator_location + 1)])
            replace_with_subtotal(inputs, operator_location, subtotal)

        while "-" in inputs:
            # handle_invalid(inputs)
            operator_location = inputs.index("-")
            subtotal = int(inputs[(operator_location - 1)]) - int(inputs[(operator_location + 1)])
            replace_with_subtotal(inputs, operator_location, subtotal)

        while "+" in inputs:
            # handle_invalid(inputs)
            operator_location = inputs.index("+")
            subtotal = int(inputs[(operator_location - 1)]) + int(inputs[(operator_location + 1)])
            replace_with_subtotal(inputs, operator_location, subtotal)
    except:
        raise ArgumentError('Invalid input entered.')

    if len(inputs) > 1:
        raise ArgumentError('Invalid input entered.')

    try:
        result = int(inputs[0])
    except:
        raise ArgumentError('Invalid input entered.')

    return result


# def handle_invalid(inputs):
#     if not re.match('-?\d+\s[+\-*/]\s-?\d+', " ".join(inputs[:5])):
#         raise ArgumentError('Invalid input entered.')
#     return


def replace_with_subtotal(inputs, operator_index, current_subtotal):
    """Reduces inputs list by removing the first operand and operator in the
    subexpression and replacing its second operand with the current subtotal.
    """
    inputs[(operator_index + 1)] = str(current_subtotal)
    del inputs[operator_index]
    del inputs[(operator_index - 1)]
    return


class ArgumentError(Exception):
    """Exception raised for errors in the input."""

# Uncomment below to run tests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** All tests passed. ***\n"
