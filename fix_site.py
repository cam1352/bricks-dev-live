import os
import re

def fix_encoding(html):
    html = html.replace('AEo?', '⭐')
    html = html.replace('A,??', '—')
    html = html.replace('AEoA', '☰') # mobile toggle burger icon
    html = html.replace('~', '☰')
    return html

def inject_lang_selector(html, current_lang=''):
    if 'id="lang-selector"' in html: return html # already injected
    
    # Prefix for links based on if we are in a subfolder or root
    prefix = '../' if current_lang else ''
    
    selector = f'''
        <li style="margin-left: 20px;">
            <select id="lang-selector" onchange="window.location.href=this.value" style="background: transparent; border: 1px solid var(--secondary); color: var(--primary); padding: 5px; border-radius: 4px; font-weight: bold; cursor: pointer;">
                <option value="{prefix}index.html" {'selected' if not current_lang else ''}>English</option>
                <option value="{prefix}es/index.html" {'selected' if current_lang=='es' else ''}>Español</option>
                <option value="{prefix}fr/index.html" {'selected' if current_lang=='fr' else ''}>Français</option>
                <option value="{prefix}zh/index.html" {'selected' if current_lang=='zh' else ''}>中文</option>
                <option value="{prefix}ru/index.html" {'selected' if current_lang=='ru' else ''}>Русский</option>
                <option value="{prefix}uk/index.html" {'selected' if current_lang=='uk' else ''}>Українська</option>
                <option value="{prefix}he/index.html" {'selected' if current_lang=='he' else ''}>עברית</option>
            </select>
        </li>
    '''
    return html.replace('</ul>', f'{selector}</ul>')

# 1. Fix services.html order
with open('services.html', 'r', encoding='utf-8', errors='ignore') as f:
    services = f.read()

# Swap sections using regex
comm_pattern = r'(<h2[^>]*>Commercial & Hospitality</h2>.*?</div>\s*</div>\s*</div>)'
res_pattern = r'(<h2[^>]*>Residential</h2>.*?</div>\s*</div>\s*</div>\s*</div>)'
import re
comm_match = re.search(comm_pattern, services, re.DOTALL)
res_match = re.search(res_pattern, services, re.DOTALL)

if comm_match and res_match:
    comm_text = comm_match.group(1)
    res_text = res_match.group(1)
    
    # Remove both from original text
    services = services.replace(comm_text, '<!--COMM-->')
    services = services.replace(res_text, '<!--RES-->')
    
    # Put them back with Res first
    services = services.replace('<!--COMM-->', res_text)
    services = services.replace('<!--RES-->', comm_text)

services = fix_encoding(services)
services = inject_lang_selector(services)
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services)

# 2. Process ALL HTML files for encoding and language selector
for root, dirs, files in os.walk('.'):
    # skip node_modules or .git
    if '.git' in root or '.netlify' in root: continue
    
    # detect if we are inside a lang folder
    lang_code = ''
    folder_name = os.path.basename(root)
    if folder_name in ['es', 'fr', 'zh', 'ru', 'uk', 'he']:
        lang_code = folder_name
        
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            content = fix_encoding(content)
            
            # Don't inject lang selector into blog/faq files to keep it simple, only main pages
            if 'blog-' not in file and 'faq-' not in file:
                content = inject_lang_selector(content, lang_code)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
print("Fixed encoding, reordered services, and injected language selector.")