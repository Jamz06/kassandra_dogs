from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField, TextAreaField, SelectField


class ScheduleForm(FlaskForm):
    '''
        Форма подачи заявки на занятия
    '''

    desired_day = DateField('День занятия')
    customer_name = StringField('Как к вам обращаться?')
    customer_email = StringField('E-Mail для обратной связи')
    customer_tel = StringField('Ваш телефон')
    contact_method = SelectField(
        'Предпочитаемый способ связи?',
        choices=[
            (1, 'Мессенджер'),
            (2, 'Телефон')
        ]
    )
    comment = TextAreaField(
        'Комментарий'
    )
    submit = SubmitField(
        'Записаться',
        render_kw = {'class': 'btn bnt-primary btn-block'}
    )
