import requests
from bs4 import BeautifulSoup

URL = "https://github.com/IBM/itz-support-public/tree/main/IBM-Technology-Zone/IBM-Technology-Zone-Runbooks"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

# Find all anchor tags with class "js-navigation-open" inside the file tree container
file_links = soup.select('.js-navigation-open')

# Extract file paths from the href attribute of each anchor tag
file_paths = [link['href'] for link in file_links]

# Filter out directories (ending with '/')
file_paths = [path for path in file_paths if not path.endswith('/')]

# Printing the list of file paths
print(file_paths)
