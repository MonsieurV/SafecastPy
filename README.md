# SafecastPy

A pure Python wrapper around the Safecast API.

![](/misc/safecast_logo.png?raw=true "Safecast")

By the [YtoTech members](https://www.ytotech.com/). Checkout our related [blog post](https://blog.ytotech.com/2016/03/30/radiation-watch-safecast/).

# Introduction

This library provides a pure Python interface for the [Safecast API](https://api.safecast.org/).

[Safecast](http://blog.safecast.org/) provides open hardware and platforms to measure and share data about people environments. Currently the Safecast API allows to publish radiation measurement data.

As they put it:
> We believe that having more freely available open data is better for everyone.

# Installation

You can install SafecastPy using:

```
$ pip install SafecastPy
```

# Starting out

First, you'll want to head over to https://api.safecast.org/en-US/users/sign_up and register a new account!

After you register, grab your account `API key` from the profile tab.

![](/misc/yourprofile.png?raw=true "API key")

You can also begin by testing your application on the Safecast API [development instance](http://dev.safecast.org/en-US/users/sign_up).

First, you'll want to import SafecastPy:

```python
import SafecastPy
```

## Dynamic Function Arguments

Keyword arguments to functions are mapped to the functions available for each endpoint in the Safecast API docs. Doing this allows us to be incredibly flexible in querying the Safecast API, so changes to the API aren't held up from you using them by this library.

# Basic Usage

All the method definitions can be found by reading over [SafecastPy/endpoints.py](/SafecastPy/endpoints.py).

## Initialization

Create a SafecastPy instance with your API key:

```python
import SafecastPy
safecast = SafecastPy.SafecastPy(
  api_key='YOUR_API_KEY')
```

By default it uses the Safecast API production instance. You may want to use the development instance:

```python
import SafecastPy
safecast = SafecastPy.SafecastPy(
  api_key='YOUR_API_KEY',
  api_url=SafecastPy.DEVELOPMENT_API_URL)
```

## Getting measurements

```python
# Get the 25 last added measurements.
safecast.get_measurements(order='created_at desc'))
# Use paging to navigate through the results.
for i in range(2, 10):
  safecast.get_measurements(order='created_at desc', page=i))
# You can also filter by unit.
safecast.get_measurements(unit=SafecastPy.UNIT_CPM)))
# Or date.
safecast.get_measurements(since='2015-09-08', until='2016-12-22')
# And use a combination of all of that.
safecast.get_measurements(
  since='2015-09-08', until='2016-12-22',
  unit=SafecastPy.UNIT_USV, order='created_at asc',
  page=20)
```

Get more information on the available parameters on [the API documentation](https://api.safecast.org/en-US/home).


## Add a measurement

```python
import datetime, random
measurement = safecast.add_measurement(json={
    'latitude': 49.418683,
    'longitude': 2.823469,
    'value': random.uniform(1, 10),
    'unit': SafecastPy.UNIT_CPM,
    'captured_at': datetime.datetime.utcnow().isoformat() + '+00:00',
    'device_id': 90,
    'location_name': '1 Rue du Grand Ferré, Compiègne',
    'height': 120
})
print('New measurement id: {0}'.format(measurement['id']))
```

## Retrieve a measurement

```python
safecast.get_measurement(id=52858985)
```

## Upload a bGeigie import

```python
bgeigie_import = safecast.upload_bgeigie_import(files={
      'bgeigie_import[source]': open('misc/sample_bgeigie.LOG', 'rb')
  }, data={
      'bgeigie_import[name]': 'Logging in Compiègne',
      'bgeigie_import[description]': 'Around the Université de Technologie',
      'bgeigie_import[credits]': 'by YtoTech team',
      'bgeigie_import[cities]': 'Compiègne',
      'bgeigie_import[orientation]': 'NWE',
      'bgeigie_import[height]': '100'
  })
print('New import id: {0}'.format(bgeigie_import['id']))
```

-------------------------

You enjoy the lib? You may check out [our blog](https://blog.ytotech.com).

You may also send us love-notes, ask questions or give any comment at [yoan@ytotech.com](mailto:yoan@ytotech.com).

Happy hacking!

### Contribute

Feel free to [open a new ticket](https://github.com/MonsieurV/SafecastPy/issues/new) or submit a PR to improve the lib.
