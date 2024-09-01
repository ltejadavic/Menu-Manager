import psycopg2
from menu_item import MenuItem  # Import MenuItem here

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(
            dbname="menu_db",
            user="postgres",
            password="luis0512",
            host="localhost",
            port="5433"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        item = cur.fetchone()
        cur.close()
        conn.close()
        if item:
            return MenuItem(item[1], item[2])  # item[1] is the name, item[2] is the price
        return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(
            dbname="menu_db",
            user="postgres",
            password="luis0512",
            host="localhost",
            port="5433"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items")
        items = cur.fetchall()
        cur.close()
        conn.close()
        return [MenuItem(item[1], item[2]) for item in items]