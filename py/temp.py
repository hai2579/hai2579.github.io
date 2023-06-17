from flask import Flask,render_template

app = Flask(__name__,template_folder='F:/pythonProject/dynamicDataAnalysis/templates')


@app.route('/tem')
def hello_world():
    return render_template('index.html')

@app.route('/')
def hello_world1():
    return 'hello world'

app.debug=True
app.run()
