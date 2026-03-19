# Caesar Cipher 🏛️
# Codédex

def decode_message(message, shift):
  shift = shift % 26

  decoded_message = ''

  for character in message:
    if character == ' ':
      decoded_message += ' '
    else:
      shifted_character = ord(character) - shift
      
      if shifted_character < ord('a'):
        shifted_character += 26

      decoded_message += chr(shifted_character)

  return decoded_message
