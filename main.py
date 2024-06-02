from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Определение пути к каталогу с шаблонами
template_dir = os.path.abspath('templates')

# Установка каталога с шаблонами
app.template_folder = template_dir

# Простой словарь с курсами валют
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert_currency():
    amount = float(request.args.get('amount', 0))
    from_currency = request.args.get('from_currency', 'USD')
    to_currency = request.args.get('to_currency', 'EUR')

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return render_template('error.html', message='Invalid currency code'), 400

    if amount <= 0:
        return render_template('error.html', message='Amount must be a positive number'), 400

    result = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
    converted_amount = round(result, 2)  # Округляем до двух знаков после запятой
    return render_template('result.html', amount=amount, from_currency=from_currency,
                           to_currency=to_currency, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
