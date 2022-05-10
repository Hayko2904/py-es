from flask import Flask, request
from waitress import serve
from Main import Main

app = Flask(__name__)


def startServer():
    serve(app, host="0.0.0.0", port=8200)


@app.route('/get', methods=['POST', 'GET'])
def get():
    data = request.form.get('searchable-value')
    main = Main()
    res = main.es(data)

    return res


