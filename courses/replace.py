import os

# Use the current directory where the script is located
title_suffix = ' by Deep Learning Centre Gurgaon'


courses_folder = os.path.dirname(os.path.realpath(__file__))
footer_text = '<footer>\n    <p>2018 Deep Learning Centre, Gurugram. All Rights Reserved.</p>\n</footer>'

for filename in os.listdir(courses_folder):
    if filename.endswith('.html'):
        filepath = os.path.join(courses_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, try opening the file with a different encoding
            with open(filepath, 'r', encoding='latin1') as file:
                content = file.read()


        if '<title>' in content and '</title>' in content:
            start = content.find('<title>') + len('<title>')
            end = content.find('</title>')
            title = content[start:end]
            content = content.replace(title, title + title_suffix)


        if '<footer>' in content:
            content = content.split('<footer>')[0] + footer_text + content.split('</footer>')[1]
        else:
            content = content.replace('</body>', f'{footer_text}\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

