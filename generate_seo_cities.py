import os

cities = ['Burnaby', 'Richmond', 'West Vancouver', 'Coquitlam', 'Surrey']
source_file = 'index.html'

with open(source_file, 'r', encoding='utf-8') as f:
    template = f.read()

for city in cities:
    filename = f"{city.lower().replace(' ', '-')}.html"
    
    # Replace Vancouver references with the target city
    # We replace "Vancouver" but keep the core brand intact
    city_html = template.replace('Vancouver''s', f"{city}'s")
    city_html = template.replace('Vancouver', city)
    
    # Add a specific meta description for the city
    city_html = city_html.replace(
        '<title>Brick Development | Brick General Contractor</title>',
        f'<title>Brick Development | Top General Contractor in {city}</title>\n    <meta name="description" content="Premier general contractor in {city} specializing in custom homes, commercial builds, and major renovations.">'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(city_html)
    print(f"Generated SEO page: {filename}")
