def lucky_river(river, hours):
  # first we create a copy of river
  new_river = list(river)

  # for each element in river
  for i in range(len(river)):
    # if river is green
    if river[i] == '☘️':
      # we modify each of its peers on the right
      # to be green as well based on the
      # hours that have passed
      # min(i + hours + 1, len(river)) allow us to avoid
      # an index error if it goes past the edge of the array
      for j in range(i, min(i + hours + 1, len(river))):
        new_river[j] = '☘️'

  # then we return the new river
  return new_river