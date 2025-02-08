import os
import re

# Define the file name (assuming the file is in the same directory)
file_name = 'classes.html'

# Get the current working directory (where the script is located)
file_path = os.path.join(os.getcwd(), file_name)

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Define the regex pattern to find all img tags
img_tag_pattern = re.compile(r'<img\s+([^>]*?)alt="([^"]*?)"([^>]*?)>')

# Function to update img tags
def update_img_tag(match):
    before_alt = match.group(1)
    alt_text = match.group(2)
    after_alt = match.group(3)
    new_alt_text = f'deeplearningcentre {alt_text}'
    return f'<img {before_alt}title="deeplearningcentre" alt="{new_alt_text}"{after_alt}>'

# Replace all img tags with the updated ones
updated_content = re.sub(img_tag_pattern, update_img_tag, content)

# Write the updated content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Updated all <img> tags in classes.html")

