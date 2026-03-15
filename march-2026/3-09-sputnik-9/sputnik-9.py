def calculate_descent(altitude):
  # each layer has: high boundary, low boundary, and velocity (m/s)
  layers = [
    (10000, 700, 2000),
    (700, 85, 500),
    (85, 50, 200),
    (50, 12, 75),
    (12, 0, 20),
  ]
  # we'll accumulate the total descent time here
  total_time = 0.0
  # for each atmospheric layer
  for high, low, velocity in layers:
    # if the altitude is above this layer's lower bound
    if altitude > low:
      # we cap the top at the layer's high boundary or the actual altitude
      top = min(altitude, high)
      # calculate the distance in km then convert to meters
      distance_km = top - low
      distance_m = distance_km * 1000
      # add the time to fall through this layer (distance / velocity)
      total_time += distance_m / velocity
  # return total time rounded to 1 decimal
  return round(total_time, 1)