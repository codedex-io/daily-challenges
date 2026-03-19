# Sputnik 9 🚀
# Codédex

def calculate_descent(altitude):
  if altitude > 700:
    time = (altitude - 700) / 2 + (700 - 85) / 0.5 + (85 - 50) / 0.2 + (50 - 12) / 0.075 + (12 - 0) / 0.020
  elif altitude > 85:
    time = (altitude - 85) / 0.5 + (85 - 50) / 0.2 + (50 - 12) / 0.075 + (12 - 0) / 0.020
  elif altitude > 50: 
    time = (altitude - 50) / 0.2 + (50 - 12) / 0.075 + (12-0) / 0.020
  elif altitude > 12:
    time = (altitude - 12) / 0.075 + (12-0) / 0.020
  else:
    time = altitude / 0.020
    
  return round(time, 1)
