from flask import render_template

from app import app

from app.admin import bp, queries
from app.admin.forms import ScheduleCreateForm


@bp.route('/schedules', methods=['GET'])
def schedules():
    '''
        Список рассписаний
    '''
    schedules = queries.get_scedules()

    return render_template('admin/schedules.html', schedules=schedules, title='Расписания')

@bp.route('/schedule/<int:schedule>', methods=['GET', 'POST'])
def schedule(schedule):
    '''
        Редактирование расписания
    '''
    
    
    form = ScheduleCreateForm()
    form.weekdays.choices = queries.get_weekdays()
    sched_data, sched_days, sched_ranges = queries.get_schedule(schedule)
    form.sched_id.data = schedule
    form.name.data = sched_data[0][1]

    return render_template('admin/schedule.html', title='Расписание', form=form)


@bp.route('/schedule_create', methods=['GET', 'POST'])
def schedule_create():
    '''
        Создать рассписание
    '''

    form = ScheduleCreateForm()

    return render_template('admin/schedule_create.html', form = form)


@bp.route('/content', methods = ['GET'])
def content():
    '''
        Редактирование контента сайта
    '''

    return render_template('admin/content.html')



@bp.route('/reports', methods = ['GET'])
def reports():
    '''
        Редактирование контента сайта
    '''

    return render_template('admin/reports.html')