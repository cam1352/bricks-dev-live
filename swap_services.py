import re

with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The container section
part1 = text.split('<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px; margin-top: 40px;">Commercial & Hospitality</h2>')[0]

comm_part = '<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px; margin-top: 40px;">Commercial & Hospitality</h2>' + text.split('<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px; margin-top: 40px;">Commercial & Hospitality</h2>')[1].split('<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px;">Residential</h2>')[0]

res_part = '<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px;">Residential</h2>' + text.split('<h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px;">Residential</h2>')[1].split('<div class="fade-in" style="background: var(--primary);')[0]

part3 = '<div class="fade-in" style="background: var(--primary);' + text.split('<div class="fade-in" style="background: var(--primary);')[1]

# Swap them
final_text = part1 + res_part + comm_part + part3

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(final_text)

# Also apply this to all translated folders
languages = ['es', 'fr', 'zh', 'ru', 'uk', 'he']
import shutil
import os
for lang in languages:
    if os.path.exists(f"{lang}/services.html"):
        shutil.copy('services.html', f"{lang}/services.html")