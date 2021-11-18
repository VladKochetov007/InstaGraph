# from instabot import Bot
from instagrapi import Client
from typing import List
from . import settings


class Bot:
    def __int__(self):
        self.client = Client()
        self.client.login(username=settings.main_user['username'],
                          password=settings.main_user['password'])

    def get_subscribers(self, name):
        return self.client.user_followers(self.get_id_from_username(name))

    def get_subscribes(self, name):
        return self.client.user_following(self.get_id_from_username(name))

    def get_username_from_user_id(self, id_):
        return self.client.username_from_user_id(id_)

    def get_id_from_username(self, name):
        return self.client.user_id_from_username(name)

    def get_description(self, name):
        return self.client.account_info()


class Person(object):
    subscribes: List[object] = []
    subscribers: List[object] = []
    name: str
    id: object
    desc: str = 'NULL'

    def __init__(self, name='NULL'):
        self.name = name
        self.subscribers = get_usernames(bot.get_subscribers(self.name))
        self.subscribes = get_usernames(bot.get_subscribes(self.name))
        self.id = bot.get_id_from_username(self.name)
        self.desc = bot.


def get_usernames(id_list: List[str]) -> List[str]:
    return [bot.get_username_from_user_id(ID) for ID in id_list]


bot = Bot()
