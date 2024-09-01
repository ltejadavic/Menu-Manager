import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        conn = psycopg2.connect(
            dbname="menu_db",
            user="postgres",
            password="luis0512",
            host="localhost",  # Adjust if necessary
            port="5433"        # Adjust if necessary
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                    (self.item_name, self.item_price))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = psycopg2.connect(
            dbname="menu_db",
            user="postgres",
            password="luis0512",
            host="localhost",  # Adjust if necessary
            port="5433"        # Adjust if necessary
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.item_name,))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        conn = psycopg2.connect(
            dbname="menu_db",
            user="postgres",
            password="luis0512",
            host="localhost",  # Adjust if necessary
            port="5433"        # Adjust if necessary
        )
        cur = conn.cursor()
        cur.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                    (new_name, new_price, self.item_name))
        conn.commit()
        cur.close()
        conn.close()
        self.item_name = new_name
        self.item_price = new_price