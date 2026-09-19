import os
import re

directories_to_fix = ['es', 'fr', 'zh', 'he', 'ru', 'uk', 'blog', 'faq']

for directory in directories_to_fix:
    if not os.path.exists(directory): continue
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Fix CSS and JS
            content = content.replace('href="assets/', 'href="../assets/')
            content = content.replace('src="assets/', 'src="../assets/')
            
            # Fix root links (about, contact, etc.) to point back to root, 
            # EXCEPT index.html which should stay in the language folder, unless it's blog/faq
            if directory in ['blog', 'faq']:
                content = content.replace('href="index.html"', 'href="../index.html"')
                content = content.replace('href="about.html"', 'href="../about.html"')
                content = content.replace('href="services.html"', 'href="../services.html"')
                content = content.replace('href="projects.html"', 'href="../projects.html"')
                content = content.replace('href="contact.html"', 'href="../contact.html"')
            else:
                # In language folders, we didn't translate about/services/etc., so they must link back to root
                content = content.replace('href="about.html"', 'href="../about.html"')
                content = content.replace('href="services.html"', 'href="../services.html"')
                content = content.replace('href="projects.html"', 'href="../projects.html"')
                content = content.replace('href="contact.html"', 'href="../contact.html"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Fixed asset and routing paths for all subdirectories.")