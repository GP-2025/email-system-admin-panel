
from flask import session
from api import getNewTokenFromLogin

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
    
    new_token = getNewTokenFromLogin(email, password)
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
            raise ValueError(f"Missing required key: {key}")
    
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