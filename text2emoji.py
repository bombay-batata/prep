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
