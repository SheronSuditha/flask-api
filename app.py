from flask import Flask

app = Flask(__name__)


@app.route('/get-update', methods=['GET'])
def handle_update():
    return {
        'status': "/get-update",
        'message': "active serve"
    }


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'status': "API is active and Live!",
        'pythonversion': "latest"
    }


if __name__ == '__main__':
    app.run()
