import urllib.request
import re

def get_wikipedia_text(url):
    # Retrieve the HTML from the Wikipedia page
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    # Remove HTML tags using a regular expression
    text = re.sub(r'<[^>]+>', '', html)

    # Print the text
    print(text)

# Example usage
get_wikipedia_text('https://en.wikipedia.org/wiki/Web_scraping')
# List of common URLs
urls = [
    'https://en.wikipedia.org/wiki/Web_scraping',
    'https://en.wikipedia.org/wiki/Data_mining',
    'https://en.wikipedia.org/wiki/Machine_learning'
]

# Loop through the URLs and print the result
for url in urls:
    print(f"Content from {url}:")
    get_wikipedia_text(url)
    print("\n" + "="*80 + "\n")