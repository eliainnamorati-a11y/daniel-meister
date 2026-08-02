import os
import glob
import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace .JPG, .jpg, .PNG, .png, .HEIC, .heic with .webp
    # Only if the .webp file actually exists in the directory!
    
    # We can do a regex find for src="..." or url(...) and check if .webp exists
    # but a simpler way is to find all generated .webp files and replace their counterparts
    
    webp_files = []
    for d in ["images", "timeline pics", "."]:
        webp_files.extend(glob.glob(f"{d}/*.webp"))
        
    for webp in webp_files:
        base = os.path.splitext(webp)[0]
        # possible original extensions
        for ext in [".jpg", ".jpeg", ".png", ".HEIC", ".heic", ".JPG", ".PNG", ".JPEG"]:
            orig = base + ext
            # escape for regex
            orig_escaped = orig.replace(" ", "%20")
            webp_escaped = webp.replace(" ", "%20")
            
            # standard replacement
            content = content.replace(orig, webp)
            # URL encoded replacement
            content = content.replace(orig_escaped, webp_escaped)
            
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    for f in glob.glob("*.html"):
        update_file(f)
    for f in glob.glob("*.css"):
        update_file(f)
