// Water Day 💧
// shercodes

function leakyPipe(volume, leak, hours, threshold) {
  let currentVolume = volume; // Initial volume
  const lossRate = leak; // Percentage per hour
  const iterations = hours; // Number of hours
  let waterRemaining = 0; // Result
  
  for (let i = 0; i < iterations; i++) {
    currentVolume = currentVolume * [1 - (lossRate / 100)]; // Calculates the volume after each hour passed.
    if (currentVolume >= threshold) {
      waterRemaining = Number(currentVolume.toFixed(2));
    } else {
      waterRemaining = -1;
    }
  }

  return waterRemaining;
}