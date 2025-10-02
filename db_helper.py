import pymysql

DB_CONFIG = dict(
    host = 'localhost',
    user = 'root',
    password = 'js990129',
    db = 'items',
    charset = 'utf8'
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)
    
    def verify_user(self, username, password):
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, password))
                count, = cur.fetchone()
                return count == 1
            
    def insert_user(self, username, password):
        sql1 = 'SELECT COUNT(*) FROM users WHERE username = %s OR password = %s'
        sql2 = 'INSERT INTO users (username, password) VALUES (%s, %s)'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql1, (username, password))
                count, = cur.fetchone()
                if count == 1:
                    return count == 1
                else:
                    cur.execute(sql2, (username, password))
                    conn.commit()
                    return count == 1
    
    def fetch_fruits(self):
        sql = 'SELECT * FROM fruits ORDER BY fruit_id'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_rev(self):
        sql = 'SELECT * FROM fruits ORDER BY fruit_id DESC'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    
    def fetch_fruits_order_by_name(self):
        sql = 'SELECT * FROM fruits ORDER BY name'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_order_by_price(self):
        sql = 'SELECT * FROM fruits ORDER BY price'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_order_by_price_rev(self):
        sql = 'SELECT * FROM fruits ORDER BY price DESC'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_order_by_amount(self):
        sql = 'SELECT * FROM fruits ORDER BY amount'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_order_by_amount_rev(self):
        sql = 'SELECT * FROM fruits ORDER BY amount DESC'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    def fetch_fruits_order_by_date(self):
        sql = 'SELECT * FROM fruits ORDER BY date'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_fruits_order_by_date_rev(self):
        sql = 'SELECT * FROM fruits ORDER BY date DESC'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()   
    
    def insert_fruit(self, name, price, amount, add_date):
        sql = 'INSERT INTO fruits (name, price, amount, date) VALUES (%s, %s, %s, %s)'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, price, amount, add_date))
                    conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    def update_name_info(self, new_name, target):
        sql = 'UPDATE fruits SET name = %s WHERE name = %s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (new_name, target))
                    conn.commit()
                    return True
            except Exception:
                conn.rollback()
                return False
            
    def update_price_info(self, new_price, target):
        sql = 'UPDATE fruits SET price = %s WHERE name = %s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (new_price, target))
                    conn.commit()
                    return True
            except Exception:
                conn.rollback()
                return False
    
    def update_amount_info(self, new_amount, target):
        sql = 'UPDATE fruits SET amount = %s WHERE name = %s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (new_amount, target))
                    conn.commit()
                    return True
            except Exception:
                conn.rollback()
                return False
            
    def search_fruit_info(self, name):
        sql = 'SELECT * FROM fruits WHERE name = %s'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, name)
                return cur.fetchall()
    
    def delete_fruit(self, target):
        sql = 'DELETE FROM fruits WHERE name = %s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (target))
                    conn.commit()
                    return True
            except Exception:
                conn.rollback()
                return False
            
    def fetch_date_fruits(self, sel_date):
        sql = 'SELECT * FROM fruits WHERE date = %s'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, sel_date)
                return cur.fetchall()