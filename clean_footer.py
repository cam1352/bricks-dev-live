import os
import re

# 1. Create blog.html
blog_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Construction Blog | Brick Development</title>
    <link rel="stylesheet" href="/bricks-dev-live/assets/css/style.css">
</head>
<body>
    <header>
        <div class="logo"><a href="/bricks-dev-live/index.html"><img src="/bricks-dev-live/assets/images/logo.jpg" alt="Brick Development Logo"></a></div>
        <ul class="nav-links">
            <li><a href="/bricks-dev-live/index.html">Home</a></li>
            <li><a href="/bricks-dev-live/about.html">About</a></li>
            <li><a href="/bricks-dev-live/services.html">Services</a></li>
            <li><a href="/bricks-dev-live/projects.html">Projects</a></li>
            <li><a href="/bricks-dev-live/contact.html">Contact</a></li>
        </ul>
    </header>
    <section class="container" style="margin-top: 100px; min-height: 60vh;">
        <h1 style="color: var(--primary);">Construction Blog</h1>
        <p>Explore our latest insights on Vancouver construction, custom homes, and commercial renovations.</p>
        <ul style="line-height: 2; margin-top: 20px;">
'''
for i in range(1, 101):
    blog_content += f'<li><a href="/bricks-dev-live/blog/blog-{i}.html" style="color: var(--secondary);">Construction Insight #{i}</a></li>\n'
blog_content += '</ul></section></body></html>'

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_content)

# 2. Create faq.html
faq_content = blog_content.replace('Construction Blog', 'Frequently Asked Questions').replace('Construction Insight', 'FAQ Question').replace('/blog/blog-', '/faq/faq-')
with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(faq_content)

# 3. Clean up the Footer across the entire site
clean_footer = '''
    <footer class="fade-in" style="padding: 60px 5% 40px 5%; background: var(--primary); color: #ccc; line-height: 1.8; margin-top: auto; border-top: 4px solid var(--secondary);">
        <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px;">
            
            <div>
                <img src="/bricks-dev-live/assets/images/logo.jpg" alt="Brick Development" style="width: 150px; margin-bottom: 20px; border-radius: 4px;">
                <p style="color: var(--secondary); font-weight: 600; margin-bottom: 10px;">Proudly Servicing Vancouver</p>
                <p style="font-size: 0.85rem; margin-bottom: 20px;">Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Coquitlam, Surrey, Langley, New Westminster</p>
                <p style="font-size: 0.85rem;">&copy; 2026 Brick Development. All rights reserved.</p>
            </div>

            <div>
                <h4 style="color: var(--white); margin-bottom: 15px; font-size: 1.1rem; border-bottom: 1px solid #444; padding-bottom: 10px;">Resources</h4>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem; display: flex; flex-direction: column; gap: 12px;">
                    <li><a href="/bricks-dev-live/blog.html" style="color: #aaa; text-decoration: none;">&rarr; Read Our Blog (100+ Articles)</a></li>
                    <li><a href="/bricks-dev-live/faq.html" style="color: #aaa; text-decoration: none;">&rarr; Frequently Asked Questions</a></li>
                    <li><a href="/bricks-dev-live/about.html" style="color: #aaa; text-decoration: none;">&rarr; About Our Company</a></li>
                    <li><a href="/bricks-dev-live/contact.html" style="color: #aaa; text-decoration: none;">&rarr; Get a Quote</a></li>
                </ul>
            </div>

        </div>
    </footer>
'''

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            content = re.sub(r'<footer.*?</footer>', clean_footer, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Created dedicated blog.html and faq.html pages. Cleaned up the footer.")