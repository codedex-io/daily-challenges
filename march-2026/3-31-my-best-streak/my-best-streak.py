def longest_streak(progress):
  # define best and current streaks
  best_streak = 0
  current_streak = 0

  # for each day
  for day in progress:
    # if completed, add 1 to current
    if day == "✅":
      current_streak += 1
      # if current higher than best
      # replace best by current
      if current_streak > best_streak:
        best_streak = current_streak
    # else reset current
    else:
      current_streak = 0

  return best_streak