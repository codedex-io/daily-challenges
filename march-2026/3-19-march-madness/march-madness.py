def upset_probability(matchups):
  results = []

  # for each matchup
  for matchup in matchups:
    # unpack the array for easier use
    team_a, seed_a, team_b, seed_b = matchup

    # use given formula :
    # upset_probability = higher_seed / (higher_seed + lower_seed)
    ups_probability = seed_a / (seed_a + seed_b)

    # add to results array and round to 2 decimal
    results.append(round(ups_probability, 2))

  return results