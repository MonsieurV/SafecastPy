import SafecastPy
import random

safecast = SafecastPy.SafecastPy(api_url=SafecastPy.DEVELOPMENT_API_URL,
    api_key='JLpQD2hzNubQe4YxaAss')
measurements = safecast.get_measurements()
print(len(measurements))
print(measurements[0])
# TODO Paging?
measurement = safecast.get_measurement(id=measurements[0]['id'])
print(measurement)
measurement = safecast.post_measurement(json={
    'latitude': 35.6461,
    'longitude': 139.7038,
    'value': random.uniform(1, 10),
    'unit': 'test'
})
print(measurement)
delete = safecast.delete_measurement(id=measurement['id'])
print(delete)
# print(safecast.post_measurement({}))
# print(safecast.post_measurement({}).text)
# TODO Update? PUT?

# http://dev.safecast.org/en-US/users/764
# http://dev.safecast.org/en-US/users/764/measurements
