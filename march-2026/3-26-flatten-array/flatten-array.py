def flatten(lst):
  # first let's init a var for the flattened array
  flat_array = []

  # for each item in the list
  for i in lst:
    # if we detect another array inside of it
    # we re-apply the function recursively
    if isinstance(i, list):
      flat_array.extend(flatten(i))
    # otherwise we simply append it
    else:
      flat_array.append(i)

  # finally we return the flattened array
  return flat_array