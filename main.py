# В файле main.py импортируем app из модуля app:
from app import app

# Используем условие для проверки, что скрипт запускается напрямую:
if __name__ == "__main__":
    app.run(debug=True)