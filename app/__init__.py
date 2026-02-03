from flask import Flask

app = Flask(__name__)
app.secret_key = "supersecretkey"

from app import user_route