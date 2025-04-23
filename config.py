import os

os.environ["FLASK_APP"] = "app.py"
os.environ["FLASK_ENV"] = "development"
os.environ["FLASK_DEBUG"] = "1"

os.environ["API_BASE_URL"] = "https://emailingsystemapi.runasp.net"
os.environ["API_ACCESS_TOKEN"] = ""