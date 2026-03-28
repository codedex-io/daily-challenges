def days_to_infect(city):
  days = 0

  while True:
    # list to store who gets infected this round
    newly_infected = []

    # for each cell in the grid
    for i in range(len(city)):
      for j in range(len(city[i])):
        if city[i][j] == '🧟':
          # check the 4 neighbors
          if i > 0 and city[i-1][j] == '👤':
            newly_infected.append((i-1, j))
          if i < len(city) - 1 and city[i+1][j] == '👤':
            newly_infected.append((i+1, j))
          if j > 0 and city[i][j-1] == '👤':
            newly_infected.append((i, j-1))
          if j < len(city[i]) - 1 and city[i][j+1] == '👤':
            newly_infected.append((i, j+1))

    # if nobody new go infected, spreading has stopped
    if not newly_infected:
      break

    # infect everyone in the list at the same time
    for i, j in newly_infected:
      city[i][j] = '🧟'

    days += 1

  # if any healthy people are left, they can never be reached
  for i in city:
    if '👤' in i:
      return -1

  return days