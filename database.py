import sqlite3
from datetime import datetime

con = sqlite3.connect('E:\\Python\\Bots\\OptiTime\\database.db')

cursorObj = con.cursor()


def chek_user(id):
    cursorObj.execute(f'SELECT id FROM user_info')
    data = cursorObj.fetchall()
    print(data)
    if (id,) in data:
        return True
    return False

