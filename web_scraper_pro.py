import requests
from bs4 import BeautifulSoup
import csv

# --- ZenithAuto: Data Extraction Tool ---

def extract_website_data(url):
    """
    Function to scrape titles and links from a real news website.
    """
    print(f"[+] Connecting to: {url}")
    
    # Headers to mimic a real browser
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        
        # Logic for Hacker News (ycombinator.com)
        for item in soup.select('.titleline > a')[:10]:
            data = {
                'title': item.get_text().strip(),
                'link': item['href']
            }
            articles.append(data)
            
        return articles
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def save_to_csv(data, filename="zenith_output.csv"):
    """
    Saves the extracted list into a clean CSV file.
    """
    if not data:
        return
        
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"[+] Data successfully saved to {filename}")

# Main execution
if __name__ == "__main__":
    # Using a real, stable URL for the screenshot
    target_url = "https://news.ycombinator.com"
    scraped_data = extract_website_data(target_url)
    
    if scraped_data:
        save_to_csv(scraped_data)
        print("--- Process Completed by ZenithAuto ---")