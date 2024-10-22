import sqlite3

db = sqlite3.connect('admin.db')
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin(
               awqat TEXT,
               baxasi INTERGER,
               photo text
)''')


async def add_to_db(awqat,baxasi,photo):
    cursor.execute('''
INSERT INTO admin(awqat,baxasi,photo)
                   VALUES(?,?,?)
''',(awqat,baxasi,photo))
    db.commit

async def show_admin():
    cursor.execute('SELECT * FROM admin')
    return cursor.fetchall()