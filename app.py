from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "This is index page"

@app.route("/users/<user>")
def userGet(user):
    response = "hello" + user
    return response

@app.route('/users/<user>/postQuery', methods=['POST'])
def userQuery(user):
    print('Printing post request',request)
    json = request.get_json()
    print('json:',json)
    return jsonify({'you sent this': json['a']})

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000)
    