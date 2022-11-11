from flask import Flask,request,render_template
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('/home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
