from flask import render_template, send_from_directory

from app import app

from app.forms import ScheduleForm

@app.route('/')
@app.route('/index')
def index():
    '''
        Главная странца
    '''
    form = ScheduleForm()
    return render_template('index.html', form=form)

