
from flask import Blueprint, render_template, request, jsonify, redirect
import db
import tools

admin_events_bp = Blueprint('admin_events', __name__, url_prefix='/admin')


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_events_bp.route('/events', methods=["GET"])
def admin_events_get():
    conn = db.connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM events;")
    events = cursor.fetchall()
    
    if events:
        events = events.__reversed__()

    cursor.close()
    conn.close()

    return render_template('admin/admin_events.html', events=events)


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_events_bp.route('/add_event', methods=["POST"])
def admin_events_post():
    if not request.form or not request.files:
        return jsonify({"error": "Invalid input"}), 400
    
    event_name = request.form["event_name"]
    event_location = request.form["event_location"]
    event_date = request.form["event_date"]
    event_image = request.files["event_image"]

    event_image_filename = tools.upload_file(event_image)
    if not event_image_filename:
        return jsonify({"error": "Error uploading image"}), 400
    
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO events (event_name, event_location, event_date, event_image_filename)
        VALUES ("{event_name}", "{event_location}", "{event_date}", "{event_image_filename}");
    """)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin/events')


# ---------------------------------------
# DELETE METHOD
# ---------------------------------------
@admin_events_bp.route('/delete_event', methods=["POST"])
def admin_events_delete():
    if not request.form:
        return jsonify({"error": "Invalid input"}), 400

    print(request.form)

    event_id = request.form["event_id"]
    event_image_filename = request.form["event_image_filename"]
    
    # Delete item form db
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM events WHERE event_id = {event_id};")
    conn.commit()
    cursor.close()
    conn.close()

    # Delete item image from server
    tools.delete_file(event_image_filename)
    
    return redirect('/admin/events')