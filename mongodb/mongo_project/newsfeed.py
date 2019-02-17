import pymongo

def getPosts(db,userid):
# """
# It is similar to the function in wall.py
# Get posts of your followings.
# There can be a few options to sort the posts such as posting date or alphabetical order of following's name.
# """
#

    if '_id' in db.posts.index_information().keys():
        pass
    else : db.posts.create_index([('_id', pymongo.ASCENDING)])

    followings_list = db.user.find_one({"_id":userid})["followings"]
    followings_posts_id_list = []


    for users in followings_list:
        if db.posts.find_one({"id":users}):
            for idx in db.posts.find({"id":users}):
                followings_posts_id_list.append(idx["_id"])
        else:
            pass

    sorted_id_list = sorted(followings_posts_id_list, reverse=True)
    iter_list = list(range(0,len(sorted_id_list),5))
    ids_iter = iter(iter_list)



    for i in range(0,len(sorted_id_list),5):
        if i!=0:
            action = input("please input 'next' --> show 5 newsfeed \n"
                           "please input 'end' or input anything --> go back page \n"
                           "action : ")
        else:
            action = 'next'

        if action=="next":
            id_iter = next(ids_iter)
            for id in sorted_id_list[id_iter:id_iter+5]:
                post = db.posts.find_one({"_id":id})
                print("post_number : ",post["_id"],'\n'
                      "writer : ",post["id"],'\n'
                      "title : ",post["title"], '\n'
                      "text : ",post["txt"],'\n'
                      "comment : ",post["comment"], '\n'
                      "like : ",post["like"], '\n'
                        )
                print("-"*80)
        elif action=="end":
            pass


def com(db,userid):
    followings_list = db.user.find_one({"_id":userid})["followings"]
    followings_posts_id_list = []


    for users in followings_list:
        if db.posts.find_one({"id":users}):
            for idx in db.posts.find({"id":users}):
                followings_posts_id_list.append(idx["_id"])
        else:
            pass

    sorted_id_list = sorted(followings_posts_id_list, reverse=True)

    # print("Your followings posts number is here", sorted_id_list)
    #
    # post_number = int(input("please input number want to comment : "))
    # want_to_com = input("please input comment :")

    if sorted_id_list:
        print("Your followings posts number is here", sorted_id_list)

        post_number = int(input("please input number want to comment : "))
        want_to_com = input("please input comment :")
        if post_number in sorted_id_list:
            db.posts.update_one({"_id": post_number}, {"$push": {"comment":{"$each":[{userid:want_to_com}]}}})
        else : print("There is no number you want")

    else : pass

def like(db,userid):
    followings_list = db.user.find_one({"_id": userid})["followings"]
    followings_posts_id_list = []

    for users in followings_list:
        if db.posts.find_one({"id": users}):
            for idx in db.posts.find({"id": users}):
                followings_posts_id_list.append(idx["_id"])
        else:
            pass

    sorted_id_list = sorted(followings_posts_id_list, reverse=True)

    # print("Your followings posts number is here", sorted_id_list)
    #
    # post_number = int(input("please input number want to comment : "))

    if sorted_id_list:
        print("Your followings posts number is here", sorted_id_list)
        post_number = int(input("please input number want to comment : "))
        do_like = input("if you input '1' then like this post elif input 0 go back : ")
        if post_number in sorted_id_list:
            if do_like == '1':
                db.posts.update({"_id": post_number}, {"$inc": {'like': 1}})
            elif do_like == '0':
                pass
            else:
                pass
        else: print("There is no number you want")

    else: pass





