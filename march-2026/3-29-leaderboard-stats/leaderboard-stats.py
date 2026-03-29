def average_time(total, completed):
  # first we split the time
  time_parts = total.split(":")

  # then we define each time unit
  hours, minutes, seconds = int(time_parts[0]), int(time_parts[1]), int(time_parts[2])

  # now we calculate the total seconds
  total_seconds = hours * 3600 + minutes * 60 + seconds

  # and we return the average
  return round(total_seconds / completed)