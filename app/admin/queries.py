# %%
import sqlite3
from flask import g
from app import app


if __name__ == '__main__':
    DATABASE = '../../kss.db'
else:
    DATABASE = 'kss.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



def get_scedules():
    '''
        Получить список расписаний
    '''
    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        query = """
            SELECT id, name FROM schedule
        """
        cursor.execute(query)
        result = cursor.fetchall()

    return result


# %%
def get_schedule(schedule):
    '''
        Получить параметры расписания
        Возвращает два списка: 
            - параметры самого расписания (название и ид)
            - список дней
            - список включенных диапазонов
    '''
    sched_data = None
    sched_days = None
    sched_ranges = None

    if type(schedule) != int:
        return sched_data, sched_ranges
    
    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        
        # Запрос, для получения параметров расписания
        query = """
            SELECT
                id, name 
            FROM
                schedule
            WHERE
                id = {id}
        """.format(id=schedule)

        cursor.execute(query)
        sched_data = cursor.fetchall()

        # Запрос на получение дней недели в расписании
        query = """
            SELECT 
                weekday 
            FROM 
                vkl_sched 
            WHERE 
                "schedule" = 1 
            GROUP BY weekday

        """
        cursor.execute(query)
        sched_days = cursor.fetchall()

        query = """
            SELECT 
                time_range 
            FROM 
                vkl_sched
            WHERE 
                "schedule" = 1
            ORDER BY time_range ASC
        """
        cursor.execute(query)
        sched_ranges = cursor.fetchall()


    return sched_data, sched_days, sched_ranges

# %%
def get_time_ranges():
    '''
        Список интервалов занятий
    '''

    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        query = """
            SELECT 
                time_range, time_val
            FROM 
                time_range
        """
        cursor.execute(query)
        result = cursor.fetchall()
    return result

# %%
def get_weekdays():
    '''
        Получить список дней недели
    '''
    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        query = """
            SELECT 
                daynum, Day_name
            FROM 
                weekdays
        """
        cursor.execute(query)
        result = cursor.fetchall()
    return result
# %%
