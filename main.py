import psycopg2


def create_db(conn):
    curs = conn.cursor()
    curs.execute("""
        CREATE TABLE IF NOT EXISTS customer (
        id SERIAL PRIMARY KEY,
        name VARCHAR(60) NOT NULL,
        last_name VARCHAR (60) NOT NULL,
        email VARCHAR(60)
        );
        """)
    curs.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        customer_id INTEGER REFERENCES customer(id),
        phone_number VARCHAR(60)
        );
        """)
    conn.commit()
    curs.close()


def add_client(conn, first_name, last_name, email, phones=None):
    curs = conn.cursor()
    curs.execute("""
            INSERT INTO customer (name, last_name, email)
            VALUES (%s, %s, %s);
            """, (first_name, last_name, email))
    conn.commit()
    curs.close()


def add_phone(conn, client_id, phone):
    curs = conn.cursor()
    curs.execute("""
    INSERT INTO phonebook (customer_id, phone_number)
    VALUES (%s, %s);
    """, (client_id, phone))


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass


def delete_phone(conn, client_id, phone):
    pass


def delete_client(conn, client_id):
    pass


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


def clean_db(conn):
    pass


with psycopg2.connect(database="customer", user="postgres", password="120290Vova") as conn:
    create_db(conn)
    add_client(conn, 'John', 'Doe', 'unknown@strange.com')
    add_phone(conn, '1', '123-45-67')

conn.close()
