def tweet_balance(tweet):
  # first we split the tweet and initialize the char count
  split_tweet = tweet.split(" ")
  char_count = 0

  # for each word in the split tweet
  for word in split_tweet:
    # if @ add 20
    if word.startswith("@"):
      char_count += 20
    # if url add 23
    elif word.startswith("http://") or word.startswith("https://"):
      char_count += 23
    else:
      # for each character
      for char in word:
        # if ascii value at least 0x1F000 it means it's an emoji
        if ord(char) >= 0x1F000:
          char_count += 2
        else:
          char_count += 1

    # space after each word
    char_count += 1

  # no trailing space after last word
  char_count -= 1

  return (140 - char_count)