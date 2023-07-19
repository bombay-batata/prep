import random

def convert_to_emoji(text):
  """Converts text to emoji.

  Args:
    text: The text to be converted.

  Returns:
    The converted text.
  """

  emoji_map = {
      "hello": "👋",
      "world": "🌎",
      "python": "🐍",
      "bard": "🤖",
  }

  converted_text = ""
  for word in text.split():
    word = word.strip()  # remove spaces from the beginning and end of the word
    if word in emoji_map:
      converted_text += emoji_map[word]
    else:
      converted_text += word

  return converted_text

def main():
  """The main function."""

  text = input("Enter a text to convert to emoji: ")
  converted_text = convert_to_emoji(text)
  print(converted_text)

if __name__ == "__main__":
  main()

  '''
  This code first creates a dictionary that maps words to their corresponding emojis. Then, it prompts the user to enter a text. The code then converts the text to emoji using the convert_to_emoji() function. However, before converting the word, the code first removes any spaces from the beginning and end of the word. This is done using the strip() method. Finally, the code prints the converted text to the console.

  '''
