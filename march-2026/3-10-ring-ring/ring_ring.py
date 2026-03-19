# Ring Ring ☎️
# Codédex

def find_unique_words(transcript):
  cleaned = ''

  for char in transcript:
    if char.isalnum() or char == ' ':
      cleaned += char

  words = cleaned.lower().split()

  return len(set(words))
