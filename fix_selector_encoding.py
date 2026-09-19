import os
import re

selector_html = '''
        <li style="margin-left: 20px;">
            <select id="lang-selector" onchange="window.location.href=this.value" style="background: transparent; border: 1px solid var(--secondary); color: var(--primary); padding: 5px; border-radius: 4px; font-weight: bold; cursor: pointer;">
                <option value="/bricks-dev-live/index.html">English</option>
                <option value="/bricks-dev-live/es/index.html">Espa&ntilde;ol</option>
                <option value="/bricks-dev-live/fr/index.html">Fran&ccedil;ais</option>
                <option value="/bricks-dev-live/zh/index.html">&#20013;&#25991;</option>
                <option value="/bricks-dev-live/ru/index.html">&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;</option>
                <option value="/bricks-dev-live/uk/index.html">&#1059;&#1082;&#1088;&#1072;&#1111;&#1085;&#1089;&#1100;&#1082;&#1072;</option>
                <option value="/bricks-dev-live/he/index.html">&#1506;&#1489;&#1512;&#1497;&#1514;</option>
            </select>
        </li>
'''

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            content = re.sub(r'<li style="margin-left: 20px;">\s*<select id="lang-selector".*?</select>\s*</li>', selector_html, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Injected HTML-entity safe language selector.")