from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicacion 1 Virtual Host Carlos Manzueta'