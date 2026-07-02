import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r') as f:
        content = f.read()
    
    old_img = '<img src="logo%20white.png" alt="Daniel Meister" style="height: 70px; width: auto;">'
    new_img = '<img src="logo%20white.png" alt="Daniel Meister" class="logo-white" style="height: 70px; width: auto;">\n          <img src="logo%20red.png" alt="Daniel Meister" class="logo-red" style="height: 70px; width: auto; display: none;">'
    
    if old_img in content:
        content = content.replace(old_img, new_img)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        # Check if it was already updated or has different formatting
        if 'class="logo-white"' not in content:
            print(f"Skipped {filename} - old image not found")

