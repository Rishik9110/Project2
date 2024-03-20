from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return 'you are in homepage'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index2',methods=['GET'])
def login():
    return render_template('index2.html')

@app.route('/login-form',methods=['POST'])
def login_from_data():
    num1 = request.form['a_val']
    num2 = request.form['a_val']
    return [int(num1),int(num2)]

@app.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app.route('/addition-form',methods=['POST'])
def addition_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)+int(num2)]



@app.route('/sub',methods=['GET'])
def addition():
    return render_template('sub.html')

@app.route('/subtraction-form',methods=['POST'])
def addition_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)-int(num2)]


app.run()


