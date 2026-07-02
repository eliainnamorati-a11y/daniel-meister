import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r') as f:
        content = f.read()
    
    old_text = '<p class="footer-name">Daniel Meister</p>'
    new_text = '<img src="logo%20white.png" alt="Daniel Meister" style="height: 40px; width: auto; margin-bottom: 0.5rem;">'
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} - text not found")
