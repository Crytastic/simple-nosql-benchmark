COLLECTION_NAME = 'flights_benchmark'
FLIGHTS_PATH = 'flights.json'
READ_QUERY = {
    'Month': 1,
    'UniqueCarrier': 'FL',
}
UPDATE_QUERY = {
    'Year': 2008,
}
UPDATE_SET = {
    'Distance': 420,
    'NewValue': True,
    'UniqueCarrier': 'ChangedCarrierName'
}
DELETE_QUERY = {
    'Year': 2008,
    'FlightNum': 579
}
