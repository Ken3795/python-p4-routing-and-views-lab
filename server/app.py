from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print the string to the console
    return text  # Display the string in the web browser
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = []
    for i in range(parameter):
        numbers.append(str(i))
    return '\n'.join(numbers) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the appropriate operation based on the URL parameters
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2
    elif operation == '%' and num2 != 0:
        result = num1 % num2
    else:
        return "Invalid operation or division by zero", 400

    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)
