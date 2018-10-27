# @Author: suveshagnihotri
# @Date:   2018-10-28T02:35:00+05:30
# @Last modified by:   suveshagnihotri
# @Last modified time: 2018-10-28T03:19:53+05:30
import pymysql
from .abs_employee import AbsEmployee
from . import QUERY, PROVIDER
import os

db_url = os.environ.get('MAIN_DB')
db_user_name = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")
database_selected_db = 'EMPLOYEE'

class Employee(AbsEmployee):
    def get_employees(self):
        db_connection = pymysql.connect(host=db_url,
                               user=db_user_name,
                               password=db_password,
                               connect_timeout=10,
                               db=database_selected_db,
                               cursorclass=pymysql.cursors.DictCursor,
                               charset='utf8')
        cursor = db_connection.cursor()
        cursor.execute(QUERY)
        print(cursor.mogrify(QUERY))
        employee_detail_list = []
        result = cursor.fetchall()
        for item in result:
            # print(item)
            employee = {
                'id': item['ID'],
                'name': item['FULL_NAME'],
                'last_name': item['LAST_NAME'],
                'first_name': item['FIRST_NAME'],
                'team_id': item['TEAM_ID']
            }
            employee_detail_list.append(employee)
        db_connection.commit()
        db_connection.close()
        print(employee_detail_list)
        return employee_detail_list
