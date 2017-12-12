import sqlite3

DB_FILE = "lite.db"

def crate_Table():
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	print("table created")
	conn.commit()
	conn.close

def insert_Data(item, quantity, price):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute(" INSERT INTO store VALUES (?, ?, ?)",(item, quantity, price))
	print("row inserted")
	conn.commit()
	conn.close

def view_Store_Items():
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows


#insert_Data("Knife", 11, 3)
print(view_Store_Items())
