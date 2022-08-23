from crypt import methods
import os
from flask import *
from flask_socketio import SocketIO
import argparse
import logging
import argparse
import pydclass.gen_img

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("module", help="display a diagram of the module")
args = parser.parse_args()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba971ddc5eb3fe749804bf2095dc6237c53e93053720b5d6d96270b26fd2c1ff'
socketio = SocketIO(app)


with open(f'{app.static_folder}/diagram.svg', ) as f:
        img = f.read()

socketio.emit('my_response',
             {'data': 'Server generated event',
              'image': img})


socketio.emit('my_response',
             {'data': 'Server generated event', 'count': 1,
              'image': img})

@app.route('/d/class')
def return_main_page():
    
    os.system('python3 '+os.getcwd()+'/gen_img.py svg '+args.module+' static/diagram')
    return render_template('main.html', module=args.module)

@app.route('/module/change')
def change_module():
    return render_template('changemodule.html', module=args.module)

@app.route('/module/form', methods=['GET'])
def get_method():
    module = request.args.get('module')
    args.module = module
    print(module)
    os.system('python3 '+os.getcwd()+'/gen_img.py svg '+args.module+' static/diagram')
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html', module=args.module)

if __name__ == "__main__":
    socketio.run(app, port=8080, host="0.0.0.0")
    