import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    
    for file in files:
        if file == 'about.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace the AI team image with an authentic project photo (exterior.jpg)
            content = content.replace(
                '<img src="/bricks-dev-live/assets/images/about_team.jpg" alt="Brick Development Executive Team"',
                '<img src="/bricks-dev-live/assets/images/exterior.jpg" alt="Completed Custom Home Project"'
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Swapped the fake-looking AI image for an authentic project photo.")