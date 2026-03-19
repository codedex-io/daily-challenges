// Pi Day 🥧
// shercodes

function cutPie(diameter, friends) {
  // Calculates the circumference of the pie.
  const circumference = Math.PI * diameter;
  
  // Divides the slices evenly among friends.
  const crustPerFriend = circumference / friends;
  
  return Number(crustPerFriend.toFixed(2));
};