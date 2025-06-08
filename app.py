from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello admin Pranjul , welcome to devops docker continue practicing '

@app.route('/health')
def health():
    return 'Server good  and running perfectly ' 
