import sqlite3

DB_FILE = "lite.db"

def Create_Table():
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	print("table created")
	conn.commit()
	conn.close

def Insert_Data(item, quantity, price):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute(" INSERT INTO store VALUES (?, ?, ?)",(item, quantity, price))
	print("row inserted")
	conn.commit()
	conn.close

def View_Store_Items():
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def Delete_Store_Item(item):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item=?",(item,))
	conn.commit()
	conn.close()

def Update_Store_Item(item, quantity, price):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
	conn.commit()
	conn.close()



Insert_Data("Knife", 11, 3)
print(View_Store_Items())
Delete_Store_Item('Knife')
print(View_Store_Items())
Update_Store_Item('Wine Glass', 99, 50)
print(View_Store_Items())
