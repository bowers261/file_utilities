import os
import re
from bs4 import BeautifulSoup


def extract_links_from_html_re(directory_path, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(directory_path):
            if filename.endswith('.html'):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as html_file:
                    html_content = html_file.read()
                    links = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', html_content)
                    for link in links:
                        file.write(link + '\n')


def extract_links_from_html_bs4(directory_path, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(directory_path):
            if filename.endswith('.html'):
                with open(os.path.join(directory_path, filename), 'r') as html_file:
                    soup = BeautifulSoup(html_file, 'html.parser')
                    links = soup.find_all('a')
                    for link in links:
                        file.write(link.get('href') + '\n')
















