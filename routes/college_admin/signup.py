from flask import Blueprint, render_template, request, jsonify, redirect, session
import db
import tools

signup_bp = Blueprint('signup', __name__)


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@signup_bp.route('/signup', methods=["GET"])
def signup_get():
    return render_template('/user/signup.html', session=session)


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@signup_bp.route('/signup', methods=["POST"])
def signup_post():
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_email, user_username FROM users")
    users = cursor.fetchall()
    
    for user in users:
        if user["user_email"] == email:
            return render_template('/user/signup.html', error_message="Email already exists")
        if user["user_username"] == username:
            return render_template('/user/signup.html', error_message="Username already exists")
        
    cursor.execute(f"""
        INSERT INTO users (user_full_name, user_email, user_username, user_password)
        VALUES ('{full_name}', '{email}', '{username}', '{password}')
    """)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/login')