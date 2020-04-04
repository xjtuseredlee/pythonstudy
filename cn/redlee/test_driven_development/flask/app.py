from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)


@app.route("/api/v1/login")
def login():
    return make_response(jsonify(
        {"status": "ok",
         "message": "you are logined in."})
        , 200)


@app.route("/api/v1/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    address = data['address']
    return make_response(jsonify({
        "status": "ok",
        "username": username,
        "email": email,
        "password": password,
        "address": address,
        "message": "your register successed."
    }), 201)


if __name__ == "__main__":
    app.run(debug=True)
