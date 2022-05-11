import json

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
    value = main.search(data)
    result = value.decode('utf-8')

    return json.dumps(result)


@app.route('/get-filtered', methods=['POST', 'GET'])
def getFiltered():
    data = request.data.decode()
    main = Main()
    res = main.search_filtered(data)

    return res


