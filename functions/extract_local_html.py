import os
import re
from bs4 import BeautifulSoup

def extract_content_from_html_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return

    for file_name in os.listdir(directory):
        if file_name.endswith(".html"):
            file_path = os.path.join(directory, file_name)
            
            with open(file_path, "r") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, "html.parser")
                divs = soup.find_all("div")
                links = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', html_content)

                with open(f"{file_name}_divs.txt", "w") as div_file:
                    for div in divs:
                        div_file.write(str(div) + "\n")

                with open(f"{file_name}_links.txt", "w") as link_file:
                    for link in links:
                        link_file.write(link + "\n")
