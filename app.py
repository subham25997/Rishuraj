import string

from flask import Flask, render_template, request, redirect, session

from app_constants import DB_SCHEMA
from init_db import get_db_connection

app = Flask(__name__)
app.secret_key = 'i am sorry'


@app.route('/')
def logout():  # put application's code here
    return redirect('/login-page')

@app.route('/logout')
def starting_route():  # put application's code here
    session.clear()
    return redirect('/login-page')


@app.route('/login/validate', methods=['POST'])
def validate_login():  # put application's code here
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * from " + DB_SCHEMA + ".user WHERE email=%s AND password=%s;";
    cur.execute(query, (email, password))
    user = cur.fetchall()
    cur.close()
    conn.close()
    if user is None or len(user) == 0:
        return render_template('error.html')
    else:
        session['user_info'] = user[0]
        return redirect('/home')


@app.route('/login-page')
def login():  # put application's code here
    user_info = session.get('user_info')
    if user_info is not None:
        return redirect('/home')
    else:
        return render_template('login.html')


@app.route('/home')
def display_home_page():
    user_info = session.get('user_info')
    if user_info is not None:
        menus = get_menus_for_this_role()
        return render_template('home.html', title='Home', menus=menus, activeMenu='Home', user_full_name=user_info[3] + ' ' + user_info[4], user_role=user_info[5])
    else:
        return redirect('/')

@app.route('/users')
def display_users_page():
    user_info = session.get('user_info')
    if user_info is not None:
        menus = get_menus_for_this_role()
        return render_template('users.html', title='User Management', menus=menus, activeMenu='Users', user_full_name=user_info[3] + ' ' + user_info[4], user_role=user_info[5])
    else:
        return redirect('/')

@app.route('/attendance')
def display_attendance_page():
    user_info = session.get('user_info')
    if user_info is not None:
        menus = get_menus_for_this_role()
        return render_template('attendance.html', title='Attendance Management', menus=menus, activeMenu='Attendance', user_full_name=user_info[3] + ' ' + user_info[4], user_role=user_info[5])
    else:
        return redirect('/')


@app.route('/customers')
def display_customers_page():
    user_info = session.get('user_info')
    if user_info is not None:
        menus = get_menus_for_this_role()
        return render_template('customers.html', title='Customers', menus=menus, activeMenu='Customers', user_full_name=user_info[3] + ' ' + user_info[4], user_role=user_info[5])
    else:
        return redirect('/')


def get_menus_for_this_role():
    role = session["user_info"][5]
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * from " + DB_SCHEMA + ".menus WHERE roles LIKE '%" + role + "%';"
    cur.execute(query)
    menus = cur.fetchall()
    cur.close()
    conn.close()
    return menus


if __name__ == '__main__':
    app.run()
