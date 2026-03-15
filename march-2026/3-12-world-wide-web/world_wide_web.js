// World Wide Web 🌐
// Codédex

function checkUrl(address) {
  if (!(address.startsWith("https://") || address.startsWith("http://"))) {
    return "invalid";
  };
  
  let domain = address.split("://");
  
  domain = domain[1];
  
  if (!domain.includes(".")) {
    return "invalid";
  };
  
  const allowedChars = /^[a-zA-Z0-9-.]+$/.test(domain);
  
  if (!allowedChars) {
    return "invalid";
  }
  
  return "valid";
};
