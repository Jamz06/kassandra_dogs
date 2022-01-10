from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectField, SelectMultipleField
from wtforms.fields.core import Label
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, Regexp, Optional
from wtforms.widgets.core import PasswordInput

from wtforms import widgets


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ScheduleCreateForm(FlaskForm):
    '''
        Форма создания рассписания
    '''

    sched_id = IntegerField()
    weekdays = MultiCheckboxField(
        label='На какие дни недели назначить',
        coerce=int
    )
    time_starts = MultiCheckboxField(
        label = 'Временные интервалы',
        coerce=int
    )
    name = StringField(
        label='Название расписания'
    )
    submit = SubmitField('Сохранить')

