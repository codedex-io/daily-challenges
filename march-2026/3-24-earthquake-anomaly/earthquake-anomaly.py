def earthquake_anomaly(readings):
  # if no readings we simply return an empty array
  if not readings:
    return []

  # first we sort the readings
  sorted_readings = sorted(readings)
  n = len(sorted_readings)
  
  # find the median
  if n % 2 == 1:
    median = sorted_readings[n // 2]
  else:
    median = (sorted_readings[n // 2 - 1] + sorted_readings[n // 2]) / 2

  # now let's find the threshold
  threshold = median * 1.5

  return [i for i, thresh in enumerate(readings) if thresh > threshold]