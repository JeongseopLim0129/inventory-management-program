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
    
    def fetch_fruits(self):
        sql = 'SELECT * FROM fruits ORDER BY fruit_id'
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
    
    def insert_fruit(self, name, price, amount):
        sql = 'INSERT INTO fruits (name, price, amount) VALUES (%s, %s, %s)'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, price, amount))
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