def find_unique_words(transcript):
  # first we create a var called cleaned
  # it will contain all the words + spaces
  cleaned = ''

  # now for each char in the transcript
  for char in transcript:
    # if (a-z, A-Z, 0-9) or a space
    if char.isalnum() or char == ' ':
      # add it to cleaned
      cleaned += char

  # then we define words
  # takes all the chars from cleaned, lowercase them
  # then split them by space
  words = cleaned.lower().split()

  # then we create a set, so that it only takes the unique words
  # and we return how much of them are they
  return len(set(words))