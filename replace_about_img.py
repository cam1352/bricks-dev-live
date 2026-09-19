import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    
    for file in files:
        if file == 'about.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace loremflickr placeholder with the new local asset
            content = re.sub(
                r'<img src="https://loremflickr\.com/800/800/construction,team\?lock=20" alt="Construction Team"',
                '<img src="/bricks-dev-live/assets/images/about_team.jpg" alt="Brick Development Executive Team"',
                content
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Replaced placeholder image on all about.html pages.")