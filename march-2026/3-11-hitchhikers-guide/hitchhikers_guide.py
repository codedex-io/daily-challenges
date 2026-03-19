# Hitchhiker's Guide 🪐
# Codédex

def minimum_components(components):
  found = {0: 0}

  for val in components:
    snapshot = dict(found)
    for total, count in snapshot.items():
      new_total = total + val
      if new_total <= 42:
        if new_total not in found or count + 1 < found[new_total]:
          found[new_total] = count + 1
  
  return found.get(42, -1)
