import psycopg2


class Customer:
    def __init__(self, key_storage):
        self.keys = key_storage
        self.conn = psycopg2.connect(database=self.keys['db_name'], user=self.keys['login'],
                                     password=self.keys['password'])
        self.curs = self.conn.cursor()

    def create_db(self):
        self.curs.execute("""
                CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(60) NOT NULL,
                last_name VARCHAR (60) NOT NULL
                );
                """)
        self.curs.execute("""
                CREATE TABLE IF NOT EXISTS communication (
                id SERIAL PRIMARY KEY,
                customer_id INTEGER REFERENCES customer(id),
                email VARCHAR(60) NOT NULL,
                telephone VARCHAR(60)
                );
                """)

    def shutdown(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()
