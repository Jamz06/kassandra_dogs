from flask import Flask

from flask_bootstrap import Bootstrap


app = Flask(__name__)

boostrap = Bootstrap(app)

# подключить конфиг
app.config.from_object('config')

# Подключить модули:
# ЦРК - абонентский отдел
# from app.admin import bp as admin_bp
# app.register_blueprint(admin_bp, url_prefix='/admin')

# Подключить маршруты
from app import views