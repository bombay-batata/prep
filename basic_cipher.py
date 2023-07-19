def caesar_cipher(text, shift):
  """Encrypts text using a Caesar cipher.

  Args:
    text: The text to be encrypted.
    shift: The number of characters to shift by.

  Returns:
    The encrypted text.
  """

  encrypted_text = ""
  for char in text:
    index = ord(char) + shift
    if index > ord("z"):
      index -= 26
    elif index < ord("a"):
      index += 26
    encrypted_text += chr(index)

  return encrypted_text

def atbash_cipher(text):
  """Encrypts text using an Atbash cipher.

  Args:
    text: The text to be encrypted.

  Returns:
    The encrypted text.
  """

  encrypted_text = ""
  for char in text:
    index = ord(char) - ord("a")
    encrypted_text += chr(ord("z") - index)

  return encrypted_text

def main():
  """The main function."""

  text = input("Enter a text to encrypt: ")
  shift = int(input("Enter a shift: "))

  encrypted_text = caesar_cipher(text, shift)
  print("The encrypted text using Caesar cipher is: " + encrypted_text)

  encrypted_text = atbash_cipher(text)
  print("The encrypted text using Atbash cipher is: " + encrypted_text)

if __name__ == "__main__":
  main()

'''
This code implements two basic ciphers: the Caesar cipher and the Atbash cipher. 
The Caesar cipher simply shifts each letter in the text by a certain number of positions. 
The Atbash cipher replaces each letter in the text with its corresponding letter at the opposite end of the alphabet
'''
