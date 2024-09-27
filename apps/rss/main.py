import requests
import xml.etree.ElementTree as ET
from colorama import Fore, Back, Style

rss_feed_url = input("Input rss feed url: ")

response = requests.get(rss_feed_url)
rss_feed = response.content

root = ET.fromstring(rss_feed)

def extract_text(element):
    if element is not None:
        return element.text
    return None

items = root.findall('.//item')
for item in items:
    title = extract_text(item.find('title'))
    link = extract_text(item.find('link'))
    description = extract_text(item.find('description'))
    
    print(Fore.RED + f"{title}")
    print(Fore.YELLOW + f"-> {link}")
    print(Style.RESET_ALL)
    print(f"{description}")

    print("\n")
