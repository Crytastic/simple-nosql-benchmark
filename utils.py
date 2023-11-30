from arango import ArangoClient
from pymongo import MongoClient
from config import COLLECTION_NAME


def pretty_print(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")  # Center the title
    print("=" * 50)


# ArangoDB Functions
def connect_to_arangodb():
    client = ArangoClient()
    return client.db('_system', username='root', password='')


def create_collection_arangodb(db):
    return db.create_collection(COLLECTION_NAME)


# MongoDB Functions
def connect_to_mongodb():
    client = MongoClient('localhost', 27017)
    return client['benchmark_db']


def create_collection_mongodb(db):
    return db[COLLECTION_NAME]
