import sqlite3

def check_db():
    databaseFile = ("data.db")
    db = sqlite3.connect(databaseFile, check_same_thread=False)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        print("DB was(1/2) found")
    except sqlite3.OperationalError:
        print("DB was(1/2) not found")
        cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT)")
        print("DB was(1/2) create...")
    try:
        cursor.execute("SELECT * FROM files")
        print("DB was(2/2) found")
    except sqlite3.OperationalError:
        print("DB was(2/2) not found")
        cursor.execute("CREATE TABLE files(user_id INT, type TEXT, code TEXT, file_id TEXT, views INT DEFAULT (0), password TEXT)")
        print("DB was(2/2) create...")

def get_users_exist(user_id):
    db = sqlite3.connect("data.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id, ))
    if cursor.fetchone() is None:
        return False
    else:
        return True

def add_user_to_db(user_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    user = [user_id]
    cursor.execute(f'''INSERT INTO users(user_id) VALUES(?)''', user)
    db.commit()

def add_new_file(user_id, type, code, file_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    data = [user_id, type, code, file_id]
    cursor.execute(f'''INSERT INTO files(user_id, type, code, file_id) VALUES(?,? ,? ,?)''', data)
    db.commit()
def add_new_file_with_password(user_id, type, code, file_id, password):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    data = [user_id, type, code, file_id, password]
    cursor.execute(f'''INSERT INTO files(user_id, type, code, file_id, password) VALUES(?,?,?,?,?)''', data)
    db.commit()
def get_file(code):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT file_id FROM files WHERE code=?", (code, ))
    fileID = cursor.fetchone()
    cursor.execute("SELECT type FROM files WHERE code=?", (code, ))
    type_file = cursor.fetchone()
    cursor.execute("SELECT views FROM files WHERE code=?", (code, ))
    views = cursor.fetchone()
    cursor.execute("SELECT password FROM files WHERE code=?", (code, ))
    password = cursor.fetchone()
    return type_file, fileID, views, password

def get_files_user(user_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT code FROM files WHERE user_id=?", (user_id, ))
    fileIDs = cursor.fetchall()
    cursor.execute("SELECT type FROM files WHERE user_id=?", (user_id, ))
    types_my_file = cursor.fetchall()
    cursor.execute("SELECT views FROM files WHERE user_id=?", (user_id, ))
    views = cursor.fetchall()
    cursor.execute("SELECT password FROM files WHERE user_id=?", (user_id, ))
    passwords = cursor.fetchall()
    return types_my_file, fileIDs, views, passwords
def update_views(code):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT views FROM files WHERE code=?", (code, ))
    views = cursor.fetchone()
    cursor.execute("""UPDATE files SET views = ? WHERE code = ?""", (int(views[0])+1, code))
    db.commit()
def delete_file(code):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("DELETE FROM files WHERE code = ?", (code, ))
    db.commit()
