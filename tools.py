from flask import session
import api
import requests
import tempfile

# ---------------------------------------
# Roles Function
# ---------------------------------------

def get_roles(lang):
    roles_en = [
        {"id": 0, "name_id": "NormalUser", "name": "Normal User"},
        {"id": 1, "name_id": "Secretary", "name": "Secretary"},
        {"id": 2, "name_id": "ViceDeanForEnvironment", "name": "Vice Dean For Environment"},
        {"id": 3, "name_id": "ViceDeanForStudentsAffairs", "name": "Vice Dean For Students Affairs"},
        {"id": 4, "name_id": "ViceDeanForPostgraduatStudies", "name": "Vice Dean Postgraduate Studies"},
        {"id": 5, "name_id": "Dean", "name": "Dean"},
        
        {"id": 6, "name_id": "VicePresidentForEnvironment", "name": "Vice President For Environment"},
        {"id": 7, "name_id": "VicePresidentForStudentsAffairs", "name": "Vice President For Students Affairs"},
        {"id": 8, "name_id": "VicePresidentForPostgraduateStudies", "name": "Vice President For Postgraduate Studies"},
        {"id": 9, "name_id": "President", "name": "President"},
        {"id": 10, "name_id": "CollegeAdmin", "name": "College Admin"},
    ]

    roles_ar = [
        {"id": 0, "name_id": "NormalUser", "name": "عادي"},
        {"id": 1, "name_id": "Secretary", "name": "سكرتير"},
        {"id": 2, "name_id": "ViceDeanForEnvironment", "name": "وكيل الكلية لشؤون البيئة"},
        {"id": 3, "name_id": "ViceDeanForStudentsAffairs", "name": "وكيل الكلية لشؤون الطلاب"},
        {"id": 4, "name_id": "ViceDeanForPostgraduatStudies", "name": "وكيل الكلية للدراسات العليا"},
        {"id": 5, "name_id": "Dean", "name": "عميد"},
        
        {"id": 6, "name_id": "VicePresidentForEnvironment", "name": "نائب رئيس الجامعة لشؤون البيئة"},
        {"id": 7, "name_id": "VicePresidentForStudentsAffairs", "name": "نائب رئيس الجامعة لشؤون الطلاب"},
        {"id": 8, "name_id": "VicePresidentForPostgraduateStudies", "name": "نائب رئيس الجامعة للدراسات العليا"},
        {"id": 9, "name_id": "President", "name": "رئيس الجامعة"},
        {"id": 10, "name_id": "CollegeAdmin", "name": "ادمن كلية"},
    ]

    roles = roles_ar if lang == "ar" else roles_en 
    if is_college_admin():
        roles = roles[:-5]
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
            raise ValueError(f"Missing required {key}")
    
    session.update({
        "id": data["userId"],
        "email": data["email"],
        "password": data["password"],
        "name": data["name"],
        "role": data["role"],
        "picture_url": data["pictureURL"],
        "signature_url": data["signatureURL"],
        "college_name": data["collegeName"],
        "college_id": data["collegeId"] ,
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
# Get Language Function
# ---------------------------------------

def get_lang():
    # Default: English - en
    return session.get("lang", "en")


# ---------------------------------------
# Update Language Function
# ---------------------------------------

def update_lang(lang):
    session["lang"] = lang


# ---------------------------------------
# Download File From URL Function
# ---------------------------------------

def download_file_from_url(url):
    if not url or url == "Empty":
        return None
    res = requests.get(url)
    if res.status_code != 200:
        return None
    print(res)
    file_name = url.split("/")[-1]
    mime_type = get_mime_type_from_url(url)
    temp_file = tempfile.SpooledTemporaryFile()
    temp_file.write(res.content)
    temp_file.seek(0)
    file = {
        "filename": file_name,
        "stream": temp_file,
        "mimetype": mime_type
    }
    return file


# ---------------------------------------
# Get Mine Type Function
# ---------------------------------------

def get_mime_type_from_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        return response.headers.get('Content-Type', None)
    except requests.RequestException as e:
        raise ValueError(f"Failed to get MIME type from URL: {e}")
