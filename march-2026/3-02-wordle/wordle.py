# Wordle 🟩
# Codédex

def wordle_guess(secret, guess):
  count = 0
  
  for i in range(5):
    if secret[i] == guess[i]:
      count = count + 1;
      
  return count
