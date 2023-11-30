import json
import benchmarks
from config import COLLECTION_NAME, FLIGHTS_PATH
from utils import connect_to_arangodb, create_collection_arangodb, connect_to_mongodb, create_collection_mongodb, \
    pretty_print


def main():
    with open(FLIGHTS_PATH, 'r') as file:
        data = json.load(file)

    pretty_print("ArangoDB Benchmark")
    arango_db = connect_to_arangodb()
    if arango_db.has_collection(COLLECTION_NAME):
        arango_db.delete_collection(COLLECTION_NAME)
    arango_flights_col = create_collection_arangodb(arango_db)

    benchmarks.insert_arangodb(arango_flights_col, data)
    benchmarks.read_arangodb(arango_flights_col)
    benchmarks.update_arangodb(arango_flights_col)
    benchmarks.delete_arangodb(arango_flights_col)

    pretty_print("MongoDB Benchmark")
    mongo_db = connect_to_mongodb()
    if COLLECTION_NAME in mongo_db.list_collection_names():
        mongo_db.drop_collection(COLLECTION_NAME)
    mongo_flights_col = create_collection_mongodb(mongo_db)

    benchmarks.insert_mongodb(mongo_flights_col, data)
    benchmarks.read_mongodb(mongo_flights_col)
    benchmarks.update_mongodb(mongo_flights_col)
    benchmarks.delete_mongodb(mongo_flights_col)


if __name__ == "__main__":
    main()
