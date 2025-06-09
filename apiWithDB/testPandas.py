from flask import Flask, jsonify
import requests
import apiWithDB.metodoRequestDB as metodoRequestDB

app = Flask(__name__)

@app.route('/')
def requestGETdata():
    rtData=metodoRequestDB.RequestDB('').requestGET()    
    metodoRequestDB.RequestDB('').closeDB()
    return jsonify(rtData)

@app.route('/<name>/<email>')
def requestPOSTdata(name, email):
    responseJson=metodoRequestDB.RequestDB('').requestPOST(name, email)
    metodoRequestDB.RequestDB('').closeDB()
    return jsonify(responseJson)

if __name__=='__main__':
    app.run(debug=True)