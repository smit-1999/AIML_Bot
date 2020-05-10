import os
import aiml,random,requests,decimal
from autocorrect import spell
import mysql.connector
from flask import Flask, request, jsonify
from url import topTrending

k = aiml.Kernel();

def learn():    
    k.learn("data/ai.aiml")
    k.learn("data/bot.aiml")

learn()

def findResponse(query):
    response = k.respond(query)
    print('bot response:' + response)
    if response[:85] == "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a":
        city = response[85:]
        api = response[:85] + "&q=" + city
        json_data = requests.get(api).json()
        print('Weather for city', json_data['main']['temp'],type(json_data['main']['temp']))
        response="Obtained from OpenMapWeather API\nMain:" + json_data['weather'][0]['main'] + " \nDescription: " \
                 +json_data['weather'][0]['description'] + "\nTemperature:" + str((json_data['main']['temp'])-273) + "Celsius"
    elif response[:28] == "http://localhost:8000/profs/":
       print('User entered a prof name,now finding courses')
       response = "You can take one of these courses taught by your favourite prof:" + getCourses(response)
    elif response == "call top trending in url.py":
        jobs = topTrending()
        response = "These are a few trending jobs,I found from Google."
        for job in jobs:
            response+= job + ","
        return response
    elif response == "":
        responseMsgs = ["Sorry,I don't understand that!","I searched through dozens of articles,but to no avail.Sorry!"
                        "I am unable to answer this.Please inform the developers!"]
        response = random.choice(responseMsgs)
    return response

def getCourses(query):
    
    a=query[28:]
    val=(a,)
    print('val:',val)
    cnx = mysql.connector.connect(user='smit', password='smit@123',
                              host='127.0.0.1',
                              database='user_chats')
    mycursor = cnx.cursor()
    
    sql = "SELECT * FROM faculty WHERE name = %s"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    dic = {}
    for x in myresult:
        str_prof = x[1].encode('ascii','ignore')
        str_subjects = x[2].encode('ascii','ignore')
        dic['prof'] = str_prof
        dic['subjects'] = str_subjects

    cnx.close();                     
    return dic['subjects']
while True:
    query = raw_input("User > ")
    response = findResponse(query)
    print(response)
    