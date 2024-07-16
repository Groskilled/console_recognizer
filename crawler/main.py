import requests
from bs4 import BeautifulSoup
from consoles import consoles
import os

def download_image(url, folder_name, num):
    response = requests.get(url)
    if response.status_code == 200:
        if not os.path.exists("../images/" + folder_name):
            os.makedirs("../images/" + folder_name)
        with open(f"../images/{folder_name}/image_{num}.jpg", 'wb') as file:
            file.write(response.content)

def search_and_download(search_term, num_images=5):
    search_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for i, image in enumerate(images[1:num_images+1]):  # Skip first image (Google logo)
        image_url = image['src']
        download_image(image_url, search_term, i)
        print(f"Downloaded image {i+1}/{num_images}")

for console in consoles:
    search_and_download(console, num_images=50)
