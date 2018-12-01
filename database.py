# -*- coding: utf-8 -*-
#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import sys
import urllib
import os
import io
import pymysql
import pymongo

from google.cloud import vision
from google.cloud.vision import types
#Twitter API credentials
consumer_key = "jfW2IxwXDeLZ0o4cna16rITPy"
consumer_secret = "FpuJHKCixotvKtKZNzwMNNIBDBxoCKz0fRA3q1zzzHGrzOwSF9"
access_key = "1041024802125963264-lVPXOYNwBss9X3jHI76Jymuis9449U"
access_secret = "v0AMgvUb092S4to6zNws8P329DoSGXiPOgyU4X2kNXo0e"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
          
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
             media_files.add(media[0]['media_url'])
    num=1
 

    i=0
    for url in media_files:
    	print(url)
    	urllib.request.urlretrieve(url,'D:/twitter/%d.jpg'%i)
    	i += 1


    

    #write tweet objects to JSON
    #file = open('tweet.json', 'w') 
    #print ("Writing tweet objects to JSON please wait...")
    #for status in alltweets:
     #   json.dump(status._json,file,sort_keys = True,indent = 4)
def videooutput(name):
    os.system("ffmpeg -f image2 -r 0.2 -i D:/twitter/%d.jpg "+name+".mp4")
    #close the file
    #print ("Done")
    #file.close()

def label(username):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'D://twitter//12.json'
    client = vision.ImageAnnotatorClient()
    dir=path
    num=0
    for root,dirname,filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.jpg':
                num = num + 1


    i=0
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase1"]
    mycol = mydb["userdata"]
    #mydict = {"username": username, "img_num": img_num, "description": desc, "description_num": c}
    #x = mycol.insert_one(mydict)

    db = pymysql.connect(host="localhost", user="root", passwd="123456", db="doc")

    cursor = db.cursor()
    cursor.execute("use doc")
    cursor.execute("DROP TABLE IF EXISTS user_data2")
    a = "CREATE TABLE user_data2 (user_name CHAR(20),image_num  INT, description_labels TEXT)"
    cursor.execute(a)
    db.commit()
    while (i<num):
        des = ""
        file_name = os.path.join(os.path.dirname(__file__),path+'/'+str(i)+'.jpg')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')
        for label in labels:
            print(label.description)
            des = des + label.description + ','
        sql = "INSERT INTO user_data2 (user_name, image_num ,description_labels) VALUES (%s,%s,%s)"
        val = (username, i, des)
        cursor.execute(sql, val)
        db.commit()
        mydict = {"username": username, "img_num": i, "description": des}
        x = mycol.insert_one(mydict)


        i += 1




#def write_text(self,(x,y),text,font_filename,font_size=11,color=(0,0,0),max_width=None,max_height=None):
 #   if isinstance(text,str):
  #      text = text.decode(self.encoding)
   # if font_size =='fill' and \

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@Ladygaga")
    path = os.getcwd()
    label('Ladygaga')
   # videooutput("Ladygaga")
    #write_text()
