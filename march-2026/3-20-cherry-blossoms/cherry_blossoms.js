// Cherry Blossoms 🌸
// shercodes

function cherryBlossoms(temps) {
  // Defines the variable for bloomDay.
  let bloomDay = -1; // -1 when there's no bloom day.

  for (let i = 4; i < temps.length; i++) {
    
    // Adds the current number plus the 4 before it.
    let sum = 0;
    for (let j = i - 4; j <= i; j++) {
      sum += temps[j];
    }

    // Calculates the 5-day average. 
    let avg = sum / 5;

    // Compares if the average is greater or equal to 15.
    if (avg >= 15) {
      bloomDay = i + 1; // i + 1 when there's a bloom day.
      return bloomDay;
    }
  }

  return bloomDay;
};