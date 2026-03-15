def minimum_components(components):
  # start with just the empty sum
  found = {0: 0}  # sum -> fewest components to reach it

  for val in components:
    # we make a copy so we don't modify the original dict while iterating
    snapshot = dict(found)
    for total, count in snapshot.items():
      new_total = total + val
      # only consider sums up to 42
      if new_total <= 42:
        # update if this is a new sum or uses fewer components
        if new_total not in found or count + 1 < found[new_total]:
          found[new_total] = count + 1
  
  # return the minimum components for 42, or -1 if not possible
  return found.get(42, -1)