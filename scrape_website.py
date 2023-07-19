import requests
import bs4

def scrape_website(url):
  """Scrapes a website and returns the HTML content."""

  response = requests.get(url)
  if response.status_code != 200:
    return None

  soup = bs4.BeautifulSoup(response.content, "html.parser")
  return soup

def main():
  """The main function."""

  url = "https://chromereleases.googleblog.com/"
  soup = scrape_website(url)
  if soup is None:
    return

  title = soup.find("title").text
  print(title)
  paragraphs = soup.find_all("p")
  for paragraph in paragraphs:
    print(paragraph.text)

if __name__ == "__main__":
  main()
