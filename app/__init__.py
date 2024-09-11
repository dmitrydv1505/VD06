from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)

# Создаем секретный ключ для защиты данных:
app.config['SECRET_KEY'] = 'you_will_never_guess'

from app import routes
