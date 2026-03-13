# Codédex Daily Challenge #1
# 6:12 4/5

# 🟨🟨🟨🟨🟨
# 🟨🟨🟨🟨🟨
# 🟨🟨🟨🟨🟨
# 🟩🟩🟩🟩🟩

secret = "CODEX"
guess = "COINS"

def wordle_guess(secret, guess):
  # Write code below 💖
  count = 0
  for i in range(5):
    if secret[i] == guess[i]:
      count = count + 1;
  print(count)
  return count

wordle_guess(secret, guess)
