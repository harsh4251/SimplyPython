"""
Registration of a user 0 tokens
Each user gets 10 tokens
Store a sentence on our db for 1 token
Retrieves his stored sentence on our db for 1 token
"""

"""
Chart of api
------------
Resource    Address     Protocol    Param               Responses
-----------------------------------------------------------------
Register    /register    POST       username,           200 OK
                                    password            202: Username already exists
Store
sentence    /store      POST        username,           200 OK
                                    password,           301: out of tokens
                                    sentence            302: Invalid username, password
Retrieve    /get        GET         username,           200 OK
sentence                            password            301: out of tokens
                                                        302: Invalid username, password
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)

api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.SentencesDatabase

users = db["Users"]

class Register(Resource):
    def post(self):
        #step1 : get posted data: 

        postedData = request.get_json()

        #get the data
        username = postedData["username"]
        password = postedData["password"]


        #hash(pw+salt) = wakfkjnkefnlkaflknn
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        if checkIfuserExists(username):
           return jsonify({
            "status": 202,
            "message":"Username already exists, pls try again"
           })


        users.insert_one({
                "Username": username, 
                "Password": hashed_pw,
                "Sentence": "",
                "tokens": 6
        })

        return jsonify({
            "status": 200,
            "message":"Yoo successfully signed up for API"
        })


def checkIfuserExists(username):
    user_count = users.find({
        "Username":username
    }).count_documents()
    if user_count>0:
       return True
    else:
       return False

def verifyPw(username, password):
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({
        "Username":username
    })[0]["Tokens"]

    return tokens

class Store(Resource):
    def post(self):
        #Step 1 get the posted data
        postedData = request.get_json()

        #Step 2 is to read the data
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        #Step 3 verify the username pw match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status":302
            }

            return jsonify(retJson)

        #Step 4 Verify user has enough tokens
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 301
            }

            return jsonify(retJson)

        #Step 5 store the sentence, take one token away  and return 200OK
        users.update({
            "Username":username
        }, {
            "$set":{
                "Sentence":sentence,
                "Tokens":num_tokens-1
                }
        })

        retJson = {
            "status":200,
            "msg":"Sentence saved successfully"
        }

        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        #Step 3 verify the username pw match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status":302
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        #MAKE THE USER PAY!
        users.update({
            "Username":username
        }, {
            "$set":{
                "Tokens":num_tokens-1
                }
        })

        sentence = users.find({
            "Username": username
        })[0]["Sentence"]

        retJson = {
            "status":200,
            "sentence": str(sentence)
        }
        return jsonify(retJson)

class Hello(Resource):
    def get(self):
        return jsonify({
            "status": 200
        })

api.add_resource(Hello, '/')
api.add_resource(Register,'/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
