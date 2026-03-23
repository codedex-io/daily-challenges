def cuddly_kittens(kittens, limit):
  # init a variable longest
  longest = 0
  
  # for each cat
  for i in range(len(kittens)):
    # for each cat on the right
    for j in range(i, len(kittens)):
      # we define a group of
      # current kitten + the one on the right
      group = kittens[i:j+1]

      # we check if group is calm
      if max(group) - min(group) <= limit:
        longest = max(longest, j - i + 1)
      else:
        break
  
  return longest