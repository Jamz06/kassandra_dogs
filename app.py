import sys
from app import app

if __name__ == '__main__':
    # Если на Лиуксе, то считаем, что это продакшен
    # Иначе, запущено на винде, для отладки
    if sys.platform == 'linux':
        app.run()
    else:
        app.run(host='0.0.0.0', port=8081, debug=True)
    # app.run(host='127.0.0.1', port=8081, debug=True)
