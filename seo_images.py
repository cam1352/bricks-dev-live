import os
import re

seo_map = {
    'logo.jpg': 'brick-development-general-contractor-vancouver-logo.jpg',
    'basement.jpg': 'vancouver-commercial-restaurant-renovation.jpg',
    'bathroom.jpg': 'luxury-bathroom-remodel-contractor-vancouver.jpg',
    'deck.jpg': 'vancouver-hotel-resort-outdoor-renovation.jpg',
    'exterior.jpg': 'custom-home-exterior-renovation-vancouver.jpg',
    'hero_coastal.jpg': 'luxury-coastal-custom-home-builder-vancouver.jpg',
    'kitchen.jpg': 'high-end-cafe-retail-renovation-vancouver.jpg',
    'painting.jpg': 'commercial-tenant-improvement-contractor-vancouver.jpg',
    'about_team.jpg': 'brick-development-construction-management-team.jpg'
}

image_dir = os.path.join('assets', 'images')

# 1. Rename physical files
for old_name, new_name in seo_map.items():
    old_path = os.path.join(image_dir, old_name)
    new_path = os.path.join(image_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

# 2. Update HTML references
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace filenames in HTML
            for old_name, new_name in seo_map.items():
                content = content.replace(old_name, new_name)
            
            # Enhance Alt Tags for better SEO
            content = content.replace('alt="Brick Development"', 'alt="Brick Development General Contractor Vancouver"')
            content = content.replace('alt="Brick Development Logo"', 'alt="Brick Development General Contractor Vancouver Logo"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Successfully renamed all images for SEO and updated HTML files.")