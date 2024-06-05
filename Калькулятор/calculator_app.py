from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')
        if operation == 'Сложение':
            result = num1 + num2
            logging.info(f'User performed addition: {num1} + {num2} = {result}')
        elif operation == 'Вычитание':
            result = num1 - num2
            logging.info(f'User performed subtraction: {num1} - {num2} = {result}')
        elif operation == 'Умножение':
            result = num1 * num2
            logging.info(f'User performed multiplication: {num1} * {num2} = {result}')
        elif operation == 'Деление':
            if num2 != 0:
                result = num1 / num2
                logging.info(f'User performed division: {num1} / {num2} = {result}')
            else:
                result = "Ошибка! Нельзя делить на ноль."
                logging.error('User tried to divide by zero')
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)