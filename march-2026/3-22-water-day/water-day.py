def leaky_pipe(volume, leak, hours, threshold):
  # for each passing hour
  for i in range(hours):
    # we calculate the new volume based on the formula
    volume = volume * (1 - leak / 100)

    # check if treshold
    if volume < threshold:
      # if volume less than threshold, it failed
      return -1

  # otherwise we return the new volume
  # once the loop is over, rounded by 2 decimals
  return round(volume, 2)