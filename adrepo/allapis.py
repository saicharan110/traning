from flask import Flask,request,jsonify,json
from pymongo import MongoClient
#from werkzeug.wrappers import response

app = Flask(__name__)

client = MongoClient('mongodb+srv://cha123:cha123@cluster0.uehz6.mongodb.net/tes')

db = client['charan']

mydb = db['sai']
@app.route("/",methods=['GET'])
def home():
    return 'hello welcome to hyderbad'


@app.route('/add',methods=['POST'])
def add():
    json = request.json
    _name = json['name']
    _email= json['email']
    _password = json['password']
    if _name and _email and _password and request.method == 'POST':

        id = mydb.insert({'name':_name,'email':_email,'password':_password})

        return jsonify('user added sucessfully')

        #response.status_code = 200

        #return response
print(id)
        
@app.route('/getusers',methods=['GET'])
def getusers():
    users =mydb.find()
    multipleuser = []
    for i in users:
        i.pop('_id')
        multipleuser.append(i)
    return jsonify({'users':multipleuser})


@app.route('/getuser/<name>',methods=['GET'])
def getuser(name):
    user=mydb.find_one({'name':str(name)})
    user.pop('_id')
    return jsonify({'users':user})


@app.route('/put/<name>',methods=['PUT'])
def put(name):
    _name1 = name
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and _name and request.method=='PUT':

        data = ({'name':_name,'email':_email,'password':_password})
        query = {'name':_name1}
        mydb.update_one(query,{'$set':data})

        return jsonify('user updated succesfully')

    

@app.route('/delete/<name>',methods=['DELETE'])
def delete(name):
    users = mydb.delete_one({'name':str(name)})
    return jsonify('user deleted sucessfully')

@app.route('/check/<email>',methods=['POST'])
def check(email):
    user=mydb.find({'email':str(email)})
    if user.count != 0:
        return jsonify('user already exist')
    

@app.route('/addnew',methods=["POST"])
def addnew():
    _json = request.json
    _name = _json["name"]
    _email= _json["email"]
    if _name and _email and request.method == 'POST':
        data = mydb.find_one({"name":_name,"email":_email})
        if _name and _email != data:
            return jsonify('user not exists')
    else:
        _name1 = _name
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _password = _json['password']

    if _name and _email and _password and _name and request.method=='PUT':

        data = ({'name':_name,'email':_email,'password':_password})
        query = {'name':_name1}
        mydb.update_one(query,{'$set':data})

        return jsonify('user updated succesfully')


if __name__     == '__main__':

    app.run(debug=True)                     