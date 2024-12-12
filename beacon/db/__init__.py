from pymongo.mongo_client import MongoClient
from beacon import conf



client = MongoClient("mongodb://{}:{}@{}:{}/{}?authSource={}".format(
    conf.database_user,
    conf.database_password,
    conf.database_host,
    conf.database_port,
    conf.database_name,
    conf.database_auth_source
)) if conf.database_host != "" else MongoClient(conf.database_uri)

beacon_db = conf.database_name
'''
client = MongoClient(
    "mongodb://root:example@127.0.0.1:27017/beacon?authSource=admin"
    #"mongodb://root:example@mongo:27017/beacon?authSource=admin"

)
'''