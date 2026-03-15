// Blood Moon 🩸
// Codédex

function bloodMoon(time) {
  
  const result = []; 
  const [hours, minutes] = time.split(":").map(Number);

  let date = new Date();
  date.setHours(hours, minutes, 0, 0);

  for (let i = 0; i < 3; i++) {
    date.setMinutes(date.getMinutes() + 168); 
    const hour = String(date.getHours()).padStart(2, "0");
    const minute = String(date.getMinutes()).padStart(2, "0");
    result.push(`${hour}:${minute}`);
  }

  return result; 
}

console.log(bloodMoon("22:30"))