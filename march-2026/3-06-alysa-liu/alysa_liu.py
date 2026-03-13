# Alysa Liu ⛸️
# Codédex

def calculate_score(elements):
  result = 0
  goe = 0

  for i in range(len(elements)):
    goe = (sum(elements[i][2]) - max(elements[i][2]) - min(elements[i][2]))/ 7
    result = result + elements[i][1] + goe * 0.1 * elements[i][1]
  
  return round(result, 1)
