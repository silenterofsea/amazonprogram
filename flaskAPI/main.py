from flask import Flask
from btEmail import bt_api


app = Flask(__name__)

@app.errorhandler(404)
def handler_404_error(err):
    return "你要干啥？"

@app.route("/index")
def index():
    return "欢迎来到Alex的世界"

@app.route("/getemail")
def getemail():
    bt_mail = bt_api()
    return bt_mail.set_mail()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)