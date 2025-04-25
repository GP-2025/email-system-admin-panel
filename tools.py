
from flask import session
import api

# ---------------------------------------
# Roles Function
# ---------------------------------------

def get_roles(lang):
    roles_en = [
        {"id": 0, "name": "Normal"},
        {"id": 1, "name": "Secretary"},
        {"id": 2, "name": "Vice Dean For Environment"},
        {"id": 3, "name": "Vice Dean Students Affairs"},
        {"id": 4, "name": "Vice Dean Postgraduate Studies"},
        {"id": 5, "name": "Dean"},
        {"id": 6, "name": "Vice President For Environment"},
        {"id": 7, "name": "Vice President For Students Affairs"},
        {"id": 8, "name": "Vice President For Postgraduate Studies"},
        {"id": 9, "name": "President"},
        {"id": 10, "name": "College Admin"},
    ]

    roles_ar = [
        {"id": 0, "name": "عادي"},
        {"id": 1, "name": "سكرتير"},
        {"id": 2, "name": "وكيل الكلية لشؤون البيئة"},
        {"id": 3, "name": "وكيل الكلية لشؤون الطلاب"},
        {"id": 4, "name": "وكيل الكلية للدراسات العليا"},
        {"id": 5, "name": "عميد"},
        {"id": 6, "name": "نائب رئيس الجامعة لشؤون البيئة"},
        {"id": 7, "name": "نائب رئيس الجامعة لشؤون الطلاب"},
        {"id": 8, "name": "نائب رئيس الجامعة للدراسات العليا"},
        {"id": 9, "name": "رئيس الجامعة"},
        {"id": 10, "name": "ادمن الكلية"},
    ]

    roles = roles_ar if lang == "ar" else roles_en 
    if is_college_admin():
        roles.pop(-1)
    return roles

# ---------------------------------------
# Is Admin Role Function
# ---------------------------------------

def is_admin():
    if session.get("role").lower() == "admin":
        return True
    return False

# ---------------------------------------
# Is College Admin Role Function
# ---------------------------------------

def is_college_admin():
    if session.get("role").lower() == "collegeadmin":
        return True
    return False

# ---------------------------------------
# get Account Role Function
# ---------------------------------------

def get_account_role():
    return session.get("role")


# ---------------------------------------
# Update Access Token Function
# ---------------------------------------

def update_token():
    email = session.get("email")
    password = session.get("password")
    
    new_token = api.getNewTokenFromLogin(email, password)
    session["access_token"] = new_token


# ---------------------------------------
# Check Session Function
# ---------------------------------------

def check_session():
    if session.get("id"):
        return True
    return False


# ---------------------------------------
# Set Session Function
# ---------------------------------------
def set_session(data):
    required_keys = [
        "userId", "email", "name", "role", "pictureURL", 
        "signatureURL", "collegeName", "collegeId", 
        "accessToken", "refreshTokenExpirationTime"
    ]
    
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required         {key}")
    
    session.update({
        "id": data["userId"],
        "email": data["email"],
        "password": data["password"],
        "name": data["name"],
        "role": data["role"],
        "picture_url": data["pictureURL"],
        "signature_url": data["signatureURL"],
        "college_name": data["collegeName"],
        "college_id": data["collegeId"],
        "access_token": data["accessToken"],
        "token_expiration_time": data["refreshTokenExpirationTime"]
    })
    
    return True


# ---------------------------------------
# Delete Session Function
# ---------------------------------------

def delete_session():
    session.clear()


# ---------------------------------------
# Check If Logged In Function
# ---------------------------------------

def is_logged_in():
    if check_session():
        return True
    False


# ---------------------------------------
# Update Language Function
# ---------------------------------------

def get_lang():
    # Default: English - en
    return session.get("lang", "en")


# ---------------------------------------
# Update Language Function
# ---------------------------------------

def update_lang(lang):
    session["lang"] = lang