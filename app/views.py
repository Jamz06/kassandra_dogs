from os import name
from flask import render_template, send_from_directory, flash

from app import app

from app.forms import ScheduleForm
from app.notify import telegram_bot_sendtext

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    '''
        Главная странца
    '''
    form = ScheduleForm()
    if form.validate_on_submit():
        message = 'Привет) Новая заявка: на {dat}, зовут {name}. Коментарий: {comment}'.format(
            comment=form.comment.data,
            dat = form.desired_day.data,
            name=form.customer_name.data
        )
        response = telegram_bot_sendtext(message)
        if response['ok']:
            flash('Успешно')
        else:
            flash('Неудалось отправить заявку( Попробуйте позже.')
        


    return render_template('index.html', form=form)

