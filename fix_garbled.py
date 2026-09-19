import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace garbled stars with ⭐⭐⭐⭐⭐
            content = re.sub(r'<div class="stars">.*?</div>', '<div class="stars">⭐⭐⭐⭐⭐</div>', content)
            
            # Replace garbled author dash with —
            content = re.sub(r'<p class="author">.*?Sarah', '<p class="author">— Sarah', content)
            content = re.sub(r'<p class="author">.*?James', '<p class="author">— James', content)
            content = re.sub(r'<p class="author">.*?Marcus', '<p class="author">— Marcus', content)
            
            # Fix garbled mobile toggle button
            content = re.sub(r'<button class="mobile-toggle">.*?</button>', '<button class="mobile-toggle">☰</button>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
print("Fixed garbled text via regex overwrite.")