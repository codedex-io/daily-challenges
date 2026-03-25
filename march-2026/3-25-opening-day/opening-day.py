def streak_counter(games):
  best_streak = 0
  current_streak = 0

  # for each game
  for game in games:
    # if it's a win
    if game == "W":
      # add 1 to current streak and return highest value
      # between best and current
      current_streak += 1
      best_streak = max(best_streak, current_streak)
    elif game == "L":
      # else if lose current streak goes to 0
      current_streak = 0

  return best_streak