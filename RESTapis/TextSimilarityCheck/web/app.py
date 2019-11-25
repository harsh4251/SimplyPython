"""
Chart of api
------------
Resource            Address     Protocol    Param               Responses
-----------------------------------------------------------------
Register            /register    POST       username,           200 OK
											password            301: Exist username
Detect similiar
of docs             /detect     POST        username,           200 OK: return similiarity & number of tokens left
											password,           301: Invalid username
											text1,              302: Invalid password
											text2               3023: Out of tokens
Refill              /refill     POST        username,           200 OK
sentence                                    admin password      301: Invalid username
											refill amount       302: Invalid admin password
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy



app=Flask(__name__)
api = Api(app)

ADMIN_PW = "admin@123"

client = MongoClient("mongodb://db:27017")
db = client.SimilarityDB
users = db["Users"]



class Register(Resource):
	def post(self):
		postedData = request.get_json()

		username = postedData["username"]
		password = postedData["password"]

		if checkIfuserExists(username):

			retJson = {
				"status" : 301,
				"message" : "Invalid username"
			}

			return jsonify(retJson)
		
		hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

		users.insert({
			"Username" : username,
			"Password" : hashed_pw,
			"Tokens" : 6
		})

		retJson = {
			"status" : 200,
			"message" : "You've successfully signed up for the API"
		}

		return jsonify(retJson)

def checkIfuserExists(username):
	user_count = users.find({
		"Username":username
	}).count()
	if user_count>0:
		return True
	else:
		return False

def verifyPw(username, password):
	if not checkIfuserExists(username):
		retJson = {
			"status" : 301,
			"message" : "Invalid username"
		}
		return False

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

class Detect(Resource):
	def post(self):
		postedData = request.get_json()

		username = postedData["username"]
		password = postedData["password"]		
		
		text1 = postedData["text1"]
		text2 = postedData["text2"]

		if not checkIfuserExists(username):
			retJson = {
				"status" : 301,
				"message" : "Invalid username"
			}
			return jsonify(retJson)

		correct_pw = verifyPw(username, password)

		if not correct_pw:
			retJson = {
				"status" : 302,
				"message" : "Invalid password"
			}
			return jsonify(retJson)

		num_tokens = countTokens(username)

		if num_tokens <= 0:
			retJson = {
				"status" : 303,
				"message" : "You're out of tokens, please refill !"
			}
			return jsonify(retJson)

		#calculate the edit distance
		nlp = spacy.load("en_core_web_sm")

		text1 = nlp(text1)
		text2 = nlp(text2)

		ratio = text1.similarity(text2)

		
		users.update(
			{"Username": username},
			{"$set":{"Tokens":num_tokens-1}}
		)

		num_tokens = countTokens(username)


		#ratio is a number between 0 and 1, 0- not-similar 1-similar

		retJson = {
			"status" : 200,
			"similarity" : ratio,
			"msg" : "Similarity score calculated successfully, {} tokens left".format(num_tokens)
		}

		return jsonify(retJson)


class Refill(Resource):
	def post(self):
		postedData = request.get_json()

		username = postedData["username"]
		password = postedData["admin_pw"]		

		refill_amount = postedData["refill"]

		# Verify username
		if not checkIfuserExists(username):
			retJson = {
				"status" : 301,
				"message" : "Invalid username"
			}
			return jsonify(retJson)
		
		if not password == ADMIN_PW:
			return jsonify({
				"status": 304,
				"message": "Invalid admin password"
			})
		
		users.update({
			"Username": username
		}, {
			"$set": {
				"Tokens": refill_amount + countTokens(username)
			}
		})

		return jsonify({
			"status": 200,
			"message": "Refilled successfully"
		})


# Register resource
api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")
api.add_resource(Refill, "/refill")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)