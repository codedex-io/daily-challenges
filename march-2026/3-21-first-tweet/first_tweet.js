// First Tweet 🐦
// shercodes

function tweetBalance(tweet) {
  let charsLeft = 140; // Limit of characters
  let count = 0; // Characters counter
  let string = tweet.split(" "); // Words array

  for (let word of string) {
    if (word.startsWith("@")) { // Usernames
      count += 20;
    } else if (word.startsWith("http://") || word.startsWith ("https://")) { // URLs
      count += 23;
    } else if (/\p{Emoji}/u.test(word)) { // Emojis
      count += 2;
    } else { // All other characters
      count += word.length;
    }
  }

  count += string.length - 1; // Adds spaces
  return charsLeft - count;
}