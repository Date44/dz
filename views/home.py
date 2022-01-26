from flask import render_template, request
from config import app
from models.users import Users

class HomeViews(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template("home/index.html", context={
            "page_title": "Главная",
            'test_message': 'Проверка транзита даных'
        })
    @staticmethod
    @app.route('/tech_panel')
    def panel():
        return render_template("home/panel.html", context={
            "page_title": "Тех-панель",
            'test_message': 'Проверка транзита даных',
            'users_list': Users.get_all_users()
        })
