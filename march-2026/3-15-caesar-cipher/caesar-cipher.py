def decode_message(message, shift):
  # in case the shift is more than 26
  # ex: a shift of 30 is the same as a shift of 4 (30 - 26)
  shift = shift % 26

  decoded_message = ""

  # for each character
  for character in message:
    # if it's a space, just add a space
    if character == " ":
      decoded_message += " "
    else:
      # otherwise find it's ASCII number using ord() and shift it 
      shifted_character = ord(character) - shift

      # in case we have a character that would go over the alphabet (x, y, z mostly)
      if shifted_character < ord('a'):
        shifted_character += 26

      # then we add its alphabet value using chr()
      decoded_message += chr(shifted_character)

  # and return the result
  return decoded_message