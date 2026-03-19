// Green Chicago River ☘️
// shercodes's solution

function luckyRiver(river, hours) {
  // Creates a new array with the same lenght as river for dyedRiver.
  let dyedRiver = Array(river.length).fill("💧");
  
  // Finds the index of each greenPatch.
  let greenPatch = [];
  for (let i = 0; i < river.length; i++) {
    if (river[i] === "☘️") {
      greenPatch.push(i);
    }
  }
  
  // Drifts the dyeSource one position to the right after every hour.
  greenPatch.forEach(dyeSource => {
    for (let p = dyeSource; p <= dyeSource + hours; p++) {
      if (p < river.length) {
        dyedRiver[p] = "☘️";
      }
    }
  });
  
  return dyedRiver;
};