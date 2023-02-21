from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    # Render the "home.html" template file
    return render_template('home.html')

# function that converts decimal to binary


def decimal_to_binary(number):
    return bin(number)

# function that converts decimal to hexadecimal


def decimal_to_hexadecimal(number):
    return hex(number)

# function that converts decimal to octal


def decimal_to_octal(number):
    return oct(number)

# function that converts binary to decimal


def binary_to_decimal(number):
    return int(number, 2)

# function that converts hexadecimal to decimal


def hexadecimal_to_decimal(number):
    return int(number, 16)

# function that converts octal to decimal


def octal_to_decimal(number):
    return int(number, 8)

# function that performs the calculation


def perform_operation(operator, number1, number2):
    if operator == '+':
        return bin(int(number1, 2) + int(number2, 2))[2:]
    elif operator == '-':
        return bin(int(number1, 2) - int(number2, 2))[2:]
    elif operator == '*':
        return bin(int(number1, 2) * int(number2, 2))[2:]
    elif operator == '/':
        return bin(int(number1, 2) / int(number2, 2))[2:]
    elif operator == '%':
        return bin(int(number1, 2) % int(number2, 2))[2:]
    else:
        return "Invalid operator"

# function that gives 1's complement of a binary number


def ones_complement(number):
    # Initialize the ones_complement variable
    ones_complement = ""

    # Loop through each digit in the binary number
    for digit in number:
        # If the digit is 0, append 1 to the ones_complement variable
        if digit == '0':
            ones_complement += '1'
        # If the digit is 1, append 0 to the ones_complement variable
        elif digit == '1':
            ones_complement += '0'

    # Return the ones_complement variable
    return ones_complement
# function that gives 1's complement of a binary number signed


def ones_complement_signed(number):
    # Initialize the ones_complement variable
    ones_complement = ""

    # Loop through each digit in the binary number
    for digit in number:
        # If the digit is 0, append 1 to the ones_complement variable
        if digit == '0':
            ones_complement += '1'
        # If the digit is 1, append 0 to the ones_complement variable
        elif digit == '1':
            ones_complement += '0'

    # Return the ones_complement variable
    return ones_complement

# function that gives 2's complement of a binary number unsigned


def twos_complement(number):
    # Initialize the twos_complement variable
    twos_complement = ""
    # Loop through each digit in the binary number
    for digit in number:
        # If the digit is 0, append 1 to the twos_complement variable
        if digit == '0':
            twos_complement += '1'
        # If the digit is 1, append 0 to the twos_complement variable
        elif digit == '1':
            twos_complement += '0'

    # Return the twos_complement variable
    return twos_complement

# function that gives 2's complement of a binary number signed


def twos_complement_signed(number):
    # Initialize the twos_complement variable
    twos_complement = ""
    # Loop through each digit in the binary number
    for digit in number:
        # If the digit is 0, append 1 to the twos_complement variable
        if digit == '0':
            twos_complement += '1'
        # If the digit is 1, append 0 to the twos_complement variable
        elif digit == '1':
            twos_complement += '0'

    # Return the twos_complement variable
    return twos_complement


@app.route('/calculate', methods=['GET', 'POST'])
# function that calculates the result
def calculate():
    if request.method == 'POST':
        number1 = request.form['number1']
        number2 = request.form['number2']
        operator = request.form['operator']

        # Perform the calculation using the existing "perform_operation" function
        result = perform_operation(operator, number1, number2)

        # Convert the numbers to different bases using the existing conversion functions
        decimal1 = binary_to_decimal(number1)
        decimal2 = binary_to_decimal(number2)
        hex1 = decimal_to_hexadecimal(decimal1)
        hex2 = decimal_to_hexadecimal(decimal2)
        oct1 = decimal_to_octal(decimal1)
        oct2 = decimal_to_octal(decimal2)

        # Render the result using the "result.html" template file
        return render_template('result.html', number1=number1, number2=number2, operator=operator, result=result, decimal1=decimal1, decimal2=decimal2, hex1=hex1, hex2=hex2, oct1=oct1, oct2=oct2)

    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
