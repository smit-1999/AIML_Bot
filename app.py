from flask import Flask, request, jsonify
import mysql.connector
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
    #app.run(host='127.0.0.1',port=8000)
    cnx = mysql.connector.connect(user='smit', password='smit@123',
                              host='127.0.0.1',
                              database='user_chats')
    mycursor = cnx.cursor()
    #mycursor.execute("create table customers(name VARCHAR(255))")

    '''
    code for inserting into db
    '''
    # sql = "INSERT INTO chats (time,userid,query,response) VALUES (%s,%s,%s,%s)"
    # val = ("24/3","smit","insert from code","hope it works!");
    # mycursor.execute(sql,val)
    # cnx.commit()
    # print(mycursor.rowcount,"record inserted")

   
    a="alice"
    val=(a,)
    mycursor.execute("SELECT * FROM chats WHERE userid=%s",val)
    myresult = mycursor.fetchall()
    for x in myresult:
         print(x)
    cnx.close();                          
    