def cherry_blossoms(temps):
  # for i starting at index 4
  # since we need at least 5 days of data
  for i in range(4, len(temps)):
    # current window of 5 days
    # taking last 4 days + today
    window = temps[i-4:i+1]

    # if the average is at least 15
    # return the day
    if sum(window) / 5 >= 15:
      return i + 1
  
  # else return -1
  return -1