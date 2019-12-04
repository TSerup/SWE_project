<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized by Thomas'
	
if __name__ == '__main__':
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized by Thomas'
	
if __name__ == '__main__':
>>>>>>> 4c7f03ef6b0aa6e474dd380893c4fb3dca724074
    app.run(debug=True,host='0.0.0.0')