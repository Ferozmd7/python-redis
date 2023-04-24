from flask import Flask
from redis import Redis
app = Flask(__name__)

@app.route('/')

def feroz():
    return "Hi feroz" 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


