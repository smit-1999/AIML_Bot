
# AIML Bot
This is a part of the CS F407 Artificial intelligence Course.

## Installation
The backend is in Python and frontend using Android.
The app has been tested locally on Android emulator and not on an Android Phone.


The database information is stored in MySQL database on local machine. For viewing and updating databases, *mySQL.txt* contains the appropriate code.

A database named *user_chats* should be created in the *mysql* system first.2 tables named *chats* and *faculty* are used for persistent storage.

The *chats* table stores the timestamp,userid, bot query and bot response in that order.
The *faculty* table stores the name of the faculty along with the courses taught.

## Setup
The backend server has to be run first,on port 8000.

The backend server can be run simply via 
```bash
$ python app.py 
```

The front end android part can be run using Android Studio.
After setting up Android Studio,and installing an Emulator for testing,simply run the play button to run.This code was run on Nexus S API 28 device at the time of development.

## Authors

 - [**Smit Shah**](https://github.com/smit-1999/)

## References

 - [For Android front end
   ](https://medium.com/@harivigneshjayapalan/android-baking-a-simple-chatbot-in-30-minutes-aiml-ff43c3269025)

