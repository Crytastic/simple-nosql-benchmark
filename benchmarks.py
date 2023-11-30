import time

from config import DELETE_QUERY, READ_QUERY, UPDATE_QUERY, UPDATE_SET
import time


def time_benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start

        if result == 0:
            raise ValueError(f"{func.__name__} returned 0, which might indicate a failed transaction (e.g. 0 inserted, "
                             f"0 deleted, etc.)")

        print(f"{func.__name__.ljust(16)}: {duration:4.4f} seconds")
        return result

    return wrapper


@time_benchmark
def insert_arangodb(collection, data):
    return collection.insert_many(data)


@time_benchmark
def insert_mongodb(collection, data):
    return collection.insert_many(data)


@time_benchmark
def update_arangodb(collection):
    return collection.update_match(UPDATE_QUERY, UPDATE_SET)


@time_benchmark
def update_mongodb(collection):
    return collection.update_many(UPDATE_QUERY, {'$set': UPDATE_SET})


@time_benchmark
def read_arangodb(collection):
    return len(list(collection.find(READ_QUERY)))


@time_benchmark
def read_mongodb(collection):
    return len(list(collection.find(READ_QUERY)))


@time_benchmark
def delete_arangodb(collection):
    return collection.delete_match(DELETE_QUERY)


@time_benchmark
def delete_mongodb(collection):
    return collection.delete_many(DELETE_QUERY)
