import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r') as f:
        content = f.read()
    
    old_text = 'style="height: 70px; width: auto;"'
    new_text = 'style="height: 56px; width: auto;"'
    old_text2 = 'style="height: 70px; width: auto; display: none;"'
    new_text2 = 'style="height: 56px; width: auto; display: none;"'
    
    if old_text in content or old_text2 in content:
        content = content.replace(old_text, new_text)
        content = content.replace(old_text2, new_text2)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} - text not found")

