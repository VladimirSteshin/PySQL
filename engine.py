import psycopg2


class Customer:
    def __init__(self, key_storage):
        self.keys = key_storage
        self.conn = psycopg2.connect(database=self.keys['db_name'], user=self.keys['login'],
                                     password=self.keys['password'])
        self.curs = self.conn.cursor()

    def clean_before(self):
        self.curs.execute("""
            DROP TABLE IF EXISTS phonebook
            """)
        self.curs.execute("""
            DROP TABLE IF EXISTS customer
            """)
        print('Done')

    def create_db(self):
        self.curs.execute("""
            CREATE TABLE IF NOT EXISTS customer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            last_name VARCHAR (60) NOT NULL,
            email VARCHAR(60)
            );
            """)
        self.curs.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER REFERENCES customer(id),
            phone_number VARCHAR(60)
            );
            """)

    def add_customer(self, name, last_name):
        self.curs.execute("""
            INSERT INTO customer (name, last_name)
            VALUES (%s, %s);
            """, (name, last_name))
        print('Customer added!')

    def add_phone(self, name, last_name, phone_number):
        self.curs.execute("""
            SELECT id FROM customer
            WHERE name = %s and last_name = %s;
            """, (name, last_name))
        cust_id = self.curs.fetchone()
        if cust_id is None:
            print('There is no such a person! Restart the program with correct data.')
        else:
            cust_id = cust_id[0]
            self.curs.execute("""
                INSERT INTO phonebook (customer_id, phone_number)
                VALUES (%s, %s);
                """, (cust_id, phone_number))
            print('Phone number added!')

    def update(self, old_name, old_last_name, new_name, new_last_name, email):
        self.curs.execute("""
                    SELECT id FROM customer
                    WHERE name = %s and last_name = %s;
                    """, (old_name, old_last_name))
        cust_id = self.curs.fetchone()
        if cust_id is None:
            print('There is no such a person! Restart the program with correct data.')
        else:
            cust_id = cust_id[0]
            self.curs.execute("""
                UPDATE customer
                SET name = %s, last_name = %s, email = %s
                WHERE id = %s;
                """, (new_name, new_last_name, email, cust_id))
            print('Updated!')

    def del_phone(self, name, last_name, phone_number):
        self.curs.execute("""
            SELECT id FROM customer
            WHERE name = %s and last_name = %s;
            """, (name, last_name))
        cust_id = self.curs.fetchone()
        if cust_id is None:
            print('There is no such a person! Restart the program with correct data.')
        else:
            cust_id = cust_id[0]
            self.curs.execute("""
                DELETE FROM phonebook
                WHERE customer_id = %s and phone_number = %s;
                """, (cust_id, phone_number))
            print('Number deleted!')

    def del_person(self, name, last_name):
        self.curs.execute("""
                    SELECT id FROM customer
                    WHERE name = %s and last_name = %s;
                    """, (name, last_name))
        cust_id = self.curs.fetchone()
        if cust_id is None:
            print('There is no such a person! Restart the program with correct data.')
        else:
            cust_id = cust_id[0]
            self.curs.execute("""
                    DELETE FROM phonebook
                    WHERE customer_id = %s;
                    """, (cust_id,))
            self.curs.execute("""
                    DELETE FROM customer
                    WHERE id = %s;
                    """, (cust_id,))
            print('Person deleted!')

    def find(self, name, last_name, phone_number, email):
        if phone_number is not None:
            self.curs.execute("""
            SELECT * FROM customer c
            JOIN phonebook p ON c.id = p.id
            WHERE phone_number = %s;
            """, (phone_number,))
        else:
            

    def shutdown(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()
