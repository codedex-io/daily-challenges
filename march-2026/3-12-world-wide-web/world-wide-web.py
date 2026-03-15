def check_url(address):
  # check if https or http
  # if so, domain takes the url without the http/s
  if address.startswith("https://"):
    domain = address[8:]
  elif address.startswith("http://"):
    domain = address[7:]
  else:
    return "invalid"
  
  # if not any dot, invalid
  if "." not in domain:
    return "invalid"
  for char in domain:
    # if char is not either a-z, A-Z, 0-9, - or . -> invalid
    if not (char.isalpha() or char.isdigit() or char == "-" or char == "."):
      return "invalid"
    
  return "valid"