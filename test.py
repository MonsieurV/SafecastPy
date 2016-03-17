# -*- coding: utf-8 -*-

import SafecastPy
import random
import datetime

# TODO use a TU lib.

# Init.
safecast = SafecastPy.SafecastPy(api_url=SafecastPy.DEVELOPMENT_API_URL,
    api_key='JLpQD2hzNubQe4YxaAss')

# Measurements.
measurements = safecast.get_measurements()
print(len(measurements))
# Paging.
print(len(safecast.get_measurements(page=5)))
# Filtering.
print(len(safecast.get_measurements(since='2015-09-08', until='2016-12-22')))
print(len(safecast.get_measurements(unit=SafecastPy.UNIT_CPM)))
# Ordering.
# Ouch! Does we really can inject SQL here? Go patch the Safecast API app.
print(len(safecast.get_measurements(order='created_at desc')))
# User measurements.
print(len(safecast.get_user_measurements(id=764)))
# Device measurements.
print(len(safecast.get_device_measurements(id=47)))
measurement = safecast.get_measurement(id=measurements[0]['id'])
print(measurement)
measurement = safecast.add_measurement(json={
    'latitude': 49.418683,
    'longitude': 2.823469,
    'value': random.uniform(1, 10),
    'unit': SafecastPy.UNIT_CPM,
    'captured_at': datetime.datetime.utcnow().isoformat() + '+00:00',
    'device_id': 90,
    'location_name': '1 Rue du Grand Ferré, Compiègne',
    # Height in cm?
    'height': 120
})
print(measurement)
safecast.delete_measurement(id=measurement['id'])

# bGeigie Imports
print(len(safecast.get_bgeigie_imports()))
print(safecast.get_bgeigie_import(id=1))
try:
    print(safecast.upload_bgeigie_import(files={
        'bgeigie_import[source]': open('misc/sample_bgeigie.LOG', 'rb')
    }, data={
        'bgeigie_import[name]': 'Logging in Compiègne',
        'bgeigie_import[description]': 'Around the Université de Technologie',
        'bgeigie_import[credits]': 'by YtoTech team',
        'bgeigie_import[cities]': 'Compiègne',
        'bgeigie_import[orientation]': 'NWE',
        'bgeigie_import[height]': '100'
    }))
except SafecastPy.SafecastPyError as spe:
    print(spe)
    assert(spe.message.get('md5sum')[0] == u'has already been taken')

# Users.
print(len(safecast.get_users()))
print(safecast.get_user(id=764))

# Devices.
print(len(safecast.get_devices()))
print(safecast.get_device(id=47))
print(safecast.add_device(json={
    'manufacturer': 'Radiation Watch',
    'model': 'Pocket Geiger Type 5',
    'sensor': 'FirstSensor X100-7 SMD'
}))

# Exceptions.
try:
    measurement = safecast.add_measurement()
except SafecastPy.SafecastPyError:
    pass
try:
    measurement = safecast.add_measurement(json={
        'latitude': 35.6461,
        'longitude': 139.7038
    })
except SafecastPy.SafecastPyError:
    pass
try:
    measurement = safecast.add_measurement(json={
        'latitude': 35.6461,
        'longitude': 139.7038,
        'unit': SafecastPy.UNIT_USV
    })
except SafecastPy.SafecastPyError:
    pass
