# main.py
from user import *
from pymongo import MongoClient
import pymongo

def mainpage(db):

    txt_main = '''
    Welcome
    1 : signup
    2 : singin
    '''
    print(txt_main)

    do = input("please input number want to do : ")

    switcher = {'1' : signup,
                '2' : signin
                }
    if do in switcher.keys():
        role_menu = switcher.get(do)
        role_menu(db)

if __name__ == "__main__":

    client = MongoClient()
    db = client.project

    mainpage(db)
