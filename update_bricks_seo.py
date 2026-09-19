import os

pages = {
    'about.html': ('Brick Development | About Our Vancouver Construction Firm', 'Learn about Brick Development, Vancouver''s trusted general contractor with over 10 years of experience in custom homes, commercial builds, and structural renovations.'),
    'services.html': ('General Contracting Services Vancouver | Brick Development', 'Explore our premium construction services in Vancouver, BC. From custom new builds to major commercial tenant improvements and residential remodeling.'),
    'projects.html': ('Construction Portfolio & Past Projects | Brick Development', 'View our portfolio of luxury custom homes, modern commercial build-outs, and major structural renovations completed across the Greater Vancouver Area.'),
    'contact.html': ('Contact Brick Development | Get a Construction Quote in Vancouver', 'Ready to start your next construction project? Contact Brick Development today for a free consultation and estimate from Vancouver''s premier general contractor.')
}

for filename, (title, desc) in pages.items():
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Simple replace for existing titles, or inject if missing
        import re
        html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>\n    <meta name="description" content="{desc}">', html, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated SEO for {filename}")
