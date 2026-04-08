// March Madness 🏀
// shercodes

function upsetProbability(matchups) {
  // Defines the array for upset.
  let upset = [];

  for (let i = 0; i < matchups.length; i++) {
    let match = matchups[i];
  
    // Determines the higher seed (seedA) and lower seed (seedB).
    const seedA = match[1];
    const seedB = match[3];
    
    // Calculates the upset probability for each matchup.
    const prob = seedA / (seedA + seedB);
    const result = Number(prob.toFixed(2));
    upset.push(result);
  }
  
  return upset;
};