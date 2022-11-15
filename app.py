from flask import Flask,request,render_template
from utils.system import get_system_info
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('/home.html')
    
    
@app.route('/system', methods=['GET'])
def system(machine_info={}):
    machine_info = get_system_info(machine_info)
    return {'status': 1, 'info': machine_info}
    

if __name__ == '__main__':
    '''
    run program
    '''
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)