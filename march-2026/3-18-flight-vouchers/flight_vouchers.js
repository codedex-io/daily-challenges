// Flight Vouchers 🏖️ 
// shercodes

function pickVoucher(vouchers, delays, max_wait) {
  // Sets the values for bestIndex and maxRatio
  let bestIndex = -1;   // If none options qualify
  let maxRatio = -1;    // The highest ratio must be greater than -1
  
  // Filters out any delay time that exceeds max_wait
  for (let i = 0; i < delays.length; i++) {
    if (delays[i] <= max_wait) { 
        
      // Calculates the ratio of each valid voucher
      const ratio = vouchers[i] / delays[i];

      // Finds the voucher with the highest ratio
      if (ratio > maxRatio) {
        maxRatio = ratio;
        bestIndex = i;
      }
    }
  }
  
  return bestIndex;
};
