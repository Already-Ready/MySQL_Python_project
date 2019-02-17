import datetime
import sys
import pymongo
from user import *
import re

def postInterface(db, user):
    # """
    # Implementing the interface to post your text.
    # There are three or more items to choose functions such as inserting and deleting a text.
    # """
    #-------------------------변수공간-----------------------------------------------

    user_name = db.user.find_one({"_id":user})["name"]

    #------------------------------------------------------------------------------

    print("-"*80)
    print(" 1 : insert Post \n"
          " 2 : delete Post \n"
          " 3 : search hashtag \n"  
          " 0 : go back userpage \n"
          )  

    do = input("please input number want to do: ")

    switcher = {'1' : insertPost,
                '2' : deletePost,
                '3' : hashtag,
                '0' : stop}

    if switcher == '0':
        userpage(db, user)
    elif do == '3':
        hashtag(db)
    else:
        role_menu = switcher.get(do)
        role_menu(db,user,user_name)

    #role_menu(db,user,user_name)



def insertPost(db, userid, username):
    # """
    # Insert user's text. You should create the post schema including,
    # for example, posting date, posting id or name, and comments.
    #
    # You should consider how to delete the text.
    # """
    #-------------------------------변수 공간---------------------------------------

    if db.posts.find_one():
        last_post_id = db.posts.find_one(sort=[('_id', pymongo.DESCENDING)])['_id']
    else:
        last_post_id = 0

    time = datetime.datetime.now()
    post_title = input("please write title : ")
    post_txt = input("please write text : ")
    tags = re.compile('#\w+')

    #-----------------------------------------------------------------------------
    print("-"*80)
    print("작성 시간 : ", time)
    print("post_number : ", last_post_id + 1)
    print("작성자 : ", username)
    print("제목 : ", post_title)
    print("내용 :", post_txt)

    db.posts.insert({"_id":last_post_id+1,"id":userid ,"name":"%s"%(username),'time':time,"title":"%s"%(post_title),"txt":"%s"%(post_txt),"comment":[],"tag":[],"like":0})

    for tag in tags.findall(post_txt):
        db.posts.update_one({"_id":last_post_id+1},{"$push":{"tag":tag}})


    if "tag_text" in db.posts.index_information().keys():
        pass
    else:
        db.posts.create_index([("tag", pymongo.TEXT)])

    print("successfully Insert")
    postInterface(db,userid)

def deletePost(db,user,user_name):
    # """
    # Delete user's text.
    # With the post schema, you can remove posts by some conditions that you specify.
    # """
    #
    # """
    # Sometimes, users make a mistake to insert or delete their text.
    # We recommend that you write the double-checking code to avoid the mistakes.
    # """
    #-------------------------------변수 공간-----------------------------------------

    user_posts = list(db.posts.find({"id":user}))
    user_posts_number = set()

    #-------------------------------------------------------------------------------

    # print(user_posts)
    if user_posts:
        print("your posts list is here : ")
        for user_post in user_posts:
            # print(user_post)
            user_posts_number.add(user_post["_id"])
            print("your post_id : ", user_post["_id"])
            print("your post_title : ", user_post["title"])
            print("-"*25)

    else: print("You don't have post. please insert_post first")

    delete_number = int(input("please input post_id want to delete (quit:0) : "))

    if delete_number == 0:
        stop(db,user,user_name)
    elif (delete_number in user_posts_number) and type(delete_number) == int:
        try:
            db.posts.delete_one({"_id":delete_number})
            print("Successfully Delete")
            postInterface(db,user)
        except Exception as e: print(e)
    else: print("please check post_id")

def stop(db,user,username):
    pass


def hashtag(db):
    want_to_find = input("please write want to find tag !!Please write like #{text} and you can write more than two hash tag\n"
                          "EX) #japan,#china : ")
    list_of_want_to_find = want_to_find.split(",")

    posts = db.posts.find({})

    if want_to_find:
        for want in list_of_want_to_find:
            for post in posts:
                if want in post["tag"]:
                    print("post_id : ", post["_id"])
                    print("time : ", post["time"])
                    print("title : ", post["title"])
                    print("text : ", post["txt"])
                    if post["comment"]:
                        for comment in post["comment"]:
                            print("comments : ",comment)
                    if post["tag"]:
                        for tag in post["tag"]:
                            print("tags : ",tag)


    else: print("plese input #{want to find txt}")


