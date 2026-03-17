// Oscars 2026 🏆
// shercodes

function oscarPool(predictions) {
  const actualWinners = ["One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"];
  const accuracy = {};
  
  // Calculates the accuracy for each friend's prediction.
  for (let friendsArray of predictions) {
    const friendsName = friendsArray[0];
    const predictedWinners = friendsArray.slice(1);
    let correctPredictions = 0
    const totalPredictions = friendsArray.length
    
    for (let i = 0; i < totalPredictions; i++) {
      if (predictedWinners[i] === actualWinners[i]){
        correctPredictions++
      }
    }
    accuracy[friendsName] = correctPredictions / totalPredictions;
  }
  
  // Finds the friend or friends with the highest accuracy.
  const highestAccuracy = Math.max(...Object.values(accuracy));
  const name = Object.keys(accuracy).filter(friendsName => accuracy[friendsName] === highestAccuracy);
  
  return name.length > 1 ? "Tie" : name[0];
}; 