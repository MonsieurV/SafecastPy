import SafecastPy

safecast = SafecastPy.SafecastPy(api_url=SafecastPy.DEVELOPMENT_API_URL)
measurements = safecast.get_measurements().json()
print(len(measurements))
