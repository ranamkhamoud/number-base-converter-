from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


def decimal_to_binary(number):
    return bin(number)


def decimal_to_hexadecimal(number):
    return hex(number)


def decimal_to_octal(number):
    return oct(number)


def binary_to_decimal(number):
    return int(number, 2)


def hexadecimal_to_decimal(number):
    return int(number, 16)


def octal_to_decimal(number):
    return int(number, 8)


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


@app.route('/calculate', methods=['GET', 'POST'])
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
