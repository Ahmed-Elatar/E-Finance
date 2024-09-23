from fastapi import FastAPI
from database import db
from models import *
from serializers import *
import requests 
import yfinance as yf
from typing import Dict
#-------------------------------------------


app =FastAPI()






"""
    recive_ticker_name :~
        function recives Ticker data from Django in JSON Format
        and call check_ticker_name function then send the response to Django

"""
@app.post("/recive-ticker/")
def receive_ticker_name(recived_data :Dict):
    
    
    # print(recived_data)
    check_result = check_ticker_name(recived_data)
    send_awnser(check_result)



    return {"message": "recived"}







"""
    send_awnser :~
        this function used to send data to django 

"""
def send_awnser(data):

    url = 'http://django:8000/recive/'  
    response = requests.post(url, json=data)
    return response
    





"""
    check_ticker_name :~
        function recives Ticker data and check is the recived symbol is valid in stock
        and add status field to data['accepted'/'not-accepted'] and saves it in mongoDB 

"""
@app.post('/check-ticker-data/')
def check_ticker_name( data :Dict ):
    
    ticker = yf.Ticker(data['symbol'])
    info =None
    try:
        info=ticker.info
        info["longName"]
    except :
        print("not valid ticker symbol")
        info = None


    if info and 'longName' in info:
        data["name"] = info['longName']
        data["status"] ="accepted"
    else:
        data["status"] ="not-accepted"

    
    db.attempts.insert_one(TickerSerializer(data))
    return data



"""
    show_attempts :~
        this function used to retrieve a list of accepted-attempts data from mongoDB
"""
@app.get("/show-accepted-attempts/")
def show_accepted_attempts():
    result =list(db.attempts.find( {'status':'accepted'},{"_id": 0}))
    return result



"""
    show_attempts :~
        this function used to retrieve a list of not-accepted-attempts data from mongoDB
"""
@app.get("/show-not-accepted-attempts/")
def show_not_accepted_attempts():
    result =list(db.attempts.find( {'status':'not-accepted'},{"_id": 0}))
    return result








