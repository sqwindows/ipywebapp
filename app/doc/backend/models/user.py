from peewee import CharField
from ipyweb.contracts.ipywebModel import ipywebModel


class user(ipywebModel):
    username = CharField()
    password = CharField()

    class Meta:
        table_name = 'user'
