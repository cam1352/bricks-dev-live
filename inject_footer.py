import os
import re

footer_html = '''
    <footer class="fade-in" style="padding: 60px 5% 40px 5%; background: var(--primary); color: #ccc; line-height: 1.8; margin-top: auto; border-top: 4px solid var(--secondary);">
        <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px;">
            
            <div>
                <img src="PREFIXassets/images/logo.jpg" alt="Brick Development" style="width: 150px; margin-bottom: 20px; border-radius: 4px;">
                <p style="color: var(--secondary); font-weight: 600; margin-bottom: 10px;">Proudly Servicing Vancouver</p>
                <p style="font-size: 0.85rem; margin-bottom: 20px;">Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Coquitlam, Surrey, Langley, New Westminster</p>
                <p style="font-size: 0.85rem;">&copy; 2026 Brick Development. All rights reserved.</p>
            </div>

            <div>
                <h4 style="color: var(--white); margin-bottom: 15px; font-size: 1.1rem; border-bottom: 1px solid #444; padding-bottom: 10px;">Construction Insights</h4>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.85rem; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                    <li><a href="PREFIXblog/blog-1.html" style="color: #aaa; text-decoration: none;">Vancouver Custom Homes</a></li>
                    <li><a href="PREFIXblog/blog-2.html" style="color: #aaa; text-decoration: none;">Laneway Houses</a></li>
                    <li><a href="PREFIXblog/blog-3.html" style="color: #aaa; text-decoration: none;">Commercial Build-outs</a></li>
                    <li><a href="PREFIXblog/blog-4.html" style="color: #aaa; text-decoration: none;">Zoning Bylaws BC</a></li>
                    <li><a href="PREFIXblog/blog-5.html" style="color: #aaa; text-decoration: none;">Renovation Costs</a></li>
                    <li><a href="PREFIXblog/blog-6.html" style="color: #aaa; text-decoration: none;">Luxury Kitchen Trends</a></li>
                    <li><a href="PREFIXblog/blog-7.html" style="color: #aaa; text-decoration: none;">Open Concept Living</a></li>
                    <li><a href="PREFIXblog/blog-8.html" style="color: #aaa; text-decoration: none;">Smart Home Integration</a></li>
                    <li><a href="PREFIXblog/blog-9.html" style="color: #aaa; text-decoration: none;">High-End Materials</a></li>
                    <li><a href="PREFIXblog/blog-10.html" style="color: #aaa; text-decoration: none;">Architectural Design</a></li>
                    <li><a href="PREFIXblog/blog-11.html" style="color: #aaa; text-decoration: none;">Heritage Restorations</a></li>
                    <li><a href="PREFIXblog/blog-12.html" style="color: #aaa; text-decoration: none;">Building Permits</a></li>
                    <li><a href="PREFIXblog/blog-13.html" style="color: #aaa; text-decoration: none;">Energy Efficiency</a></li>
                    <li><a href="PREFIXblog/blog-14.html" style="color: #aaa; text-decoration: none;">Seismic Upgrades</a></li>
                    <li><a href="PREFIXblog/blog-15.html" style="color: #aaa; text-decoration: none;">Outdoor Living Spaces</a></li>
                    <li><a href="PREFIXblog/blog-16.html" style="color: #aaa; text-decoration: none;">Basement Suites</a></li>
                    <li><a href="PREFIXblog/blog-17.html" style="color: #aaa; text-decoration: none;">Strata Renovations</a></li>
                    <li><a href="PREFIXblog/blog-18.html" style="color: #aaa; text-decoration: none;">Concrete Work</a></li>
                    <li><a href="PREFIXblog/blog-19.html" style="color: #aaa; text-decoration: none;">Project Management</a></li>
                    <li><a href="PREFIXblog/blog-20.html" style="color: #aaa; text-decoration: none;">Sustainable Building</a></li>
                </ul>
            </div>

            <div>
                <h4 style="color: var(--white); margin-bottom: 15px; font-size: 1.1rem; border-bottom: 1px solid #444; padding-bottom: 10px;">Frequently Asked Questions</h4>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.85rem; display: flex; flex-direction: column; gap: 8px;">
                    <li><a href="PREFIXfaq/faq-1.html" style="color: #aaa; text-decoration: none;">How much per square foot?</a></li>
                    <li><a href="PREFIXfaq/faq-2.html" style="color: #aaa; text-decoration: none;">Do you handle building permits?</a></li>
                    <li><a href="PREFIXfaq/faq-3.html" style="color: #aaa; text-decoration: none;">How long does a custom build take?</a></li>
                    <li><a href="PREFIXfaq/faq-4.html" style="color: #aaa; text-decoration: none;">Are you WorkSafeBC licensed?</a></li>
                    <li><a href="PREFIXfaq/faq-5.html" style="color: #aaa; text-decoration: none;">What is a BC Housing warranty?</a></li>
                    <li><a href="PREFIXfaq/faq-6.html" style="color: #aaa; text-decoration: none;">Do you use subcontractors?</a></li>
                    <li><a href="PREFIXfaq/faq-7.html" style="color: #aaa; text-decoration: none;">How do you handle change orders?</a></li>
                    <li><a href="PREFIXfaq/faq-8.html" style="color: #aaa; text-decoration: none;">Is architectural design included?</a></li>
                    <li><a href="PREFIXfaq/faq-9.html" style="color: #aaa; text-decoration: none;">What is the typical payment schedule?</a></li>
                    <li><a href="PREFIXfaq/faq-10.html" style="color: #aaa; text-decoration: none;">Can I live in the home during a renovation?</a></li>
                </ul>
            </div>

        </div>
    </footer>
'''

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root or 'blog' in root or 'faq' in root: continue
    
    # Calculate relative prefix for links
    prefix = '../' if os.path.basename(root) in ['es', 'fr', 'zh', 'ru', 'uk', 'he'] else ''
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace old footer
            content = re.sub(r'<footer.*?</footer>', footer_html.replace('PREFIX', prefix), content, flags=re.DOTALL)
            
            # Fix dropdown language names
            content = re.sub(r'<option value=".*?/index.html".*?>Espa.*?ol</option>', f'<option value="{prefix}es/index.html">Español</option>', content)
            content = re.sub(r'<option value=".*?/index.html".*?>Fran.*?ais</option>', f'<option value="{prefix}fr/index.html">Français</option>', content)
            content = re.sub(r'<option value=".*?/index.html".*?>.*?,-.*?.*?.*?</option>', f'<option value="{prefix}zh/index.html">中文</option>', content)
            
            # Simplified regex for the garbled cyrillic/hebrew
            if 'ru/index.html' in content:
                content = re.sub(r'<option value="[^"]*ru/index.html"[^>]*>.*?</option>', f'<option value="{prefix}ru/index.html">Русский</option>', content)
            if 'uk/index.html' in content:
                content = re.sub(r'<option value="[^"]*uk/index.html"[^>]*>.*?</option>', f'<option value="{prefix}uk/index.html">Українська</option>', content)
            if 'he/index.html' in content:
                content = re.sub(r'<option value="[^"]*he/index.html"[^>]*>.*?</option>', f'<option value="{prefix}he/index.html">עברית</option>', content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Injected SEO Footer and fixed language dropdown.")