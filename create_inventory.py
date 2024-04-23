import sqlite3

def create_inventory_db(db_name):
    """Create a SQLite database for the inventory management system."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            description TEXT,
                            quantity INTEGER NOT NULL,
                            price REAL NOT NULL
                          )''')

        conn.commit()
        print("Database created successfully!")
    except sqlite3.Error as e:
        print("Error creating database:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_inventory_db("inventory.db")