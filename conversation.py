import os
import aiml
from autocorrect import spell

k = aiml.Kernel();

def learn():    
    k.learn("data/ai.aiml")
    k.learn("data/bot.aiml")

learn()

while True:
    query = raw_input("User > ")
    response = k.respond(query)
    if response == "":
        response = "Sorry,I don't understand that!" 
    print "Bot > " ,response