from instagrapi import Client
from instagrapi.types import UserShort
from typing import List


class Bot:
    def __init__(self):
        self.client = Client()
        self.client.login(username=username_,
                          password=password_)

    def get_subscribers(self, name):
        return list(self.client.user_followers(self.get_id_from_username(name)).values())

    def get_subscribes(self, name):
        return list(self.client.user_following(self.get_id_from_username(name)).values())

    def get_username_from_user_id(self, id_):
        return self.client.username_from_user_id(id_)

    def get_id_from_username(self, name):
        return self.client.user_id_from_username(name)


class Person(object):
    subscribes: List[object] = []
    subscribers: List[object] = []
    name: str
    id: object
    desc: str = 'NULL'
    friends: List[object]

    def __init__(self, name='NULL', desc='NULL', picture_url='NULL'):
        self.name = name
        self.id = bot.get_id_from_username(self.name)

    def fetch_friends(self):
        self.subscribers = get_persons(bot.get_subscribers(self.name))
        self.subscribes = get_persons(bot.get_subscribes(self.name))


def get_persons(shorts: List[UserShort]) -> List[Person]:
    return [UserShort_to_Person(short) for short in shorts]

def UserShort_to_Person(usershort: UserShort):
    return Person(name=usershort.username,
                  desc=usershort.full_name,
                  picture_url=usershort.profile_pic_url)


password_: str = 'NULL'
username_: str = 'NULL'
bot: Bot

def set_main_user(username: str,
                  password: str):
    global password_
    password_ = password
    global username_
    username_ = username
    global bot
    bot = Bot()
