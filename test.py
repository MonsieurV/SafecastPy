import SafecastPy
import random

safecast = SafecastPy.SafecastPy(api_url=SafecastPy.DEVELOPMENT_API_URL,
    api_key='JLpQD2hzNubQe4YxaAss')
get = safecast.get_measurements()
print(get)
measurements = get.json()
print(len(measurements))
print(measurements[0])
get = safecast.get_measurement(measurements[0]['id'])
print(get)
measurement = get.json()
print(measurement)
post = safecast.post_measurement({
    'latitude': 35.6461,
    'longitude': 139.7038,
    'value': random.uniform(1, 10),
    'unit': 'test'
})
print(post)
print(post.json())
# print(safecast.post_measurement({}))
# print(safecast.post_measurement({}).text)
