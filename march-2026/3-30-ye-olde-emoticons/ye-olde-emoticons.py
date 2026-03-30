def emoticons_mood(message):
  # first let's define the emoticons
  happy_emoticons = [":)", ":p", "xd", ":3", "<3", "\\m/"]
  sad_emoticons = [":'(", ":(", "t(-.-t)"]

  # we init the score
  score = 0

  # now we calculate
  for emoticon in sad_emoticons:
    score -= message.lower().count(emoticon)
  for emoticon in happy_emoticons:
    score += message.lower().count(emoticon)

  # then we return the score
  return score