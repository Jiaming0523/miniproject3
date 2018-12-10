from twitter import get_all_tweets
from twitter import label
from twitter import videooutput

import pymongo
import pymysql

import mongodb as mongodb
import mysql as mysql

import os

def get_input():
    try:
        input = int(input("Enter option:"))
    except ValueError:
        print("Please input a number")
    return input

if __name__ == '__main__':
    while():
        db = pymysql.connect(host="localhost", user="root", passwd="123456", db="doc")

        cursor = db.cursor()
        cursor.execute("use doc")
        print('Menu:\n1.Get all tweets with username\n2.Show database tables\n3.Search for word')
        op = get_input()
        if(op == 1):
            name = str(input())
            twitter.ger_all_tweets(name)
            path = os.getcwd()
            twitter.label(name)
            print('Store '+name+' into mysql database and mongodb database')
        elif(op == 2):
            mysql.print_db(cursor)
            mongodb.print_db()
        elif(op == 3):
            print("Insert a Data Base to query:\n1.MySQL\n2.MongoDB")
            database = get_input()
            if (database == 1):
                mysql.search_word(cursor)
            else:
                mongo.search_word()




