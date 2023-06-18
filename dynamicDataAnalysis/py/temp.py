from flask import Flask, render_template

# 需要设置static文件夹路径和templates文件夹路径，否则无法找到文件
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/1')
def hello_world1():
    return 'hello world'


app.debug = True
app.run()
