from flask import Blueprint, render_template, request, jsonify, redirect, session
import db
import tools

login_bp = Blueprint('login', __name__)


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@login_bp.route('/login', methods=["GET"])
def login_get():
    return render_template('/user/login.html')


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@login_bp.route('/login', methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, user_username, user_password FROM users")
    users = cursor.fetchall()
    
    for user in users:
        if user["user_username"] == username and user["user_password"] == password:
            session['user_id'] = user["user_id"]
            session['user_username'] = user["user_username"]
            cursor.execute(f"""
                SELECT SUM(cart_item_quantity) AS total_items
                FROM cart_items
                INNER JOIN carts ON cart_items.cart_id = carts.cart_id
                WHERE carts.user_id = {user["user_id"]}
            """)
            result = cursor.fetchone()
            session['cart_items_count'] = int(result['total_items']) if result['total_items'] else 0
            return redirect('/')

    return render_template('/user/login.html', error_message="Invalid username or password")