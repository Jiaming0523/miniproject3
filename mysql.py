def query_user(mycursor):
    screen_name =input("Enter a user name to query: ")
    mycursor.execute("SELECT * FROM user_data WHERE username='"+screen_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)==0):
        print("No such user name")
    else:
        for user in myresult:
            print(user)

def print_db(mycursor):
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("There are ",len(myresult),"users at data base")
    print("The current data base is ")
    avg_im=0
    desc=[]
    for user in myresult:
        avg_im=avg_im+int(user[2])
        curr_des=user[3].split(',')
        for j in curr_des:
            desc.append(j)
        print(user)
    if (len(myresult)>0):
        print("Some statistics:")
        print("The most popular description is",(max(set(desc), key = desc.count)))
        print("There is an average of",str(avg_im/len(myresult)),"images per feed")
    return

def delete_db(mycursor):
    mycursor.execute("truncate user_data;")
    return

def search_word(mycursor):
    word=input("Enter a word to search: ")
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("The next user has the word",word,"in their description:")
    for user in myresult:
        desc=user[3]
        desc=desc.split(',')
        if word in desc:
            print(user[1])
