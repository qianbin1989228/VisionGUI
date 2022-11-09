# **Build_Framework**

# **1. Create Flask Project**
First, cd to the root directory of the project:
```bash
cd VisionGUI
```
Then create a .py file named app.py and input python code below to create a flask application:
```python
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"
    
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True,debug=True)
```
Then run this script to start the project:
```bash
python app.py
```
After the development server started, we can visit the website by explore:
http://127.0.0.1:5000

# **2. Prepare Front Template**

[free template](https://github.com/qianbin1989228/Free-Admin-Bootstrap-Template)