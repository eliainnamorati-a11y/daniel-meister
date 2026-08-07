import os
from PIL import Image, ImageOps
import glob

def compress_image(file_path):
    # Only process if > 300KB
    if os.path.getsize(file_path) < 300 * 1024:
        return None
        
    try:
        img = Image.open(file_path)
        img = ImageOps.exif_transpose(img) # Fix EXIF rotation
        
        # Convert RGBA to RGB for webp/jpeg if necessary, though webp supports RGBA
        
        # Resize if very large
        max_dim = 1920
        if img.width > max_dim or img.height > max_dim:
            ratio = min(max_dim / img.width, max_dim / img.height)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
        base, ext = os.path.splitext(file_path)
        new_path = base + ".webp"
        
        img.save(new_path, "webp", quality=80, method=4)
        print(f"Converted {file_path} to {new_path}")
        return new_path
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")
        return None

if __name__ == "__main__":
    directories = ["images", "timeline pics", "."]
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.PNG", "*.JPEG")
    
    for d in directories:
        for ext in extensions:
            for file_path in glob.glob(f"{d}/{ext}"):
                compress_image(file_path)
