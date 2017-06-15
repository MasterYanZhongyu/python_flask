from flask import Flask,Request,current_app

app = Flask(__name__)


from flask import request
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>',methods=['GET','POST'])
def user(name):
    return '<h1>hello , %s \n %s</h1>' % (name,app.url_map),305


if __name__ == '__main__':
    app.run(debug=True)


