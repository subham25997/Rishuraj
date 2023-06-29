# import os
import psycopg2

from app_constants import DB_SCHEMA


def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="auth_db",
        user='postgres',
        password='Ilovemyself@123'
    )


conn = get_db_connection()
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS public.user;')
cur.execute('CREATE TABLE ' + DB_SCHEMA + '.user (user_id serial PRIMARY KEY,'
                                          'email varchar (150) NOT NULL,'
                                          'password varchar (50) NOT NULL,'
                                          'first_name varchar (50) NOT NULL,'
                                          'last_name varchar (50) NOT NULL,'
                                          'role varchar (50) NOT NULL,'
                                          'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

cur.execute('DROP TABLE IF EXISTS public.menus;')
cur.execute('CREATE TABLE ' + DB_SCHEMA + '.menus (menu_id serial PRIMARY KEY,'
                                          'name varchar (150) NOT NULL,'
                                          'icon varchar (150) NOT NULL,'
                                          'link varchar (50) NOT NULL,'
                                          'roles varchar (50) NOT NULL,'
                                          'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )


# Insert data into the table
cur.execute('INSERT INTO ' + DB_SCHEMA + '.user(email, password, first_name, last_name, role)'
                                         'VALUES (%s, %s, %s, %s, %s)',
            ('rishu@gmail.com', '1234', 'Rishu', 'Singh', 'Admin')
            )

cur.execute('INSERT INTO ' + DB_SCHEMA + '.user(email, password, first_name, last_name, role)'
                                         'VALUES (%s, %s, %s, %s, %s)',
            ('subham@gmail.com', '1234', 'Subham', 'Singh', 'Supervisor')
            )

cur.execute('INSERT INTO ' + DB_SCHEMA + '.user(email, password, first_name, last_name, role)'
                                         'VALUES (%s, %s, %s, %s, %s)',
            ('namrata@gmail.com', '1234', 'Namrata', 'Singh', 'Data Entry')
            )


cur.execute('INSERT INTO ' + DB_SCHEMA + '.menus(name, icon, link, roles)'
                                         'VALUES (%s, %s, %s, %s)',
            ('Home', 'fa-home', '/home', 'Admin,Supervisor,Data Entry')
            )

cur.execute('INSERT INTO ' + DB_SCHEMA + '.menus(name, icon, link, roles)'
                                         'VALUES (%s, %s, %s, %s)',
            ('Users', 'fa-users', '/users', 'Admin')
            )

cur.execute('INSERT INTO ' + DB_SCHEMA + '.menus(name, icon, link, roles)'
                                         'VALUES (%s, %s, %s, %s)',
            ('Attendance', 'fa-address-book', '/attendance', 'Admin,Supervisor,Data Entry')
            )

cur.execute('INSERT INTO ' + DB_SCHEMA + '.menus(name, icon, link, roles)'
                                         'VALUES (%s, %s, %s, %s)',
            ('Customers', 'fa-user-tie', '/customers', 'Supervisor,Data Entry')
            )
conn.commit()

cur.close()
conn.close()
