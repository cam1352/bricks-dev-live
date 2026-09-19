import os

languages = {
    'he': {
        'title': 'בריק פיתוח | קבלן ראשי',
        'hero': 'בונים את העתיד של ונקובר',
        'subhero': 'קבלן ראשי מורשה ב-BC',
        'desc': 'קבלן ראשי מוביל המתמחה בבנייה חדשה, חללים מסחריים ושיפוצים גדולים',
        'btn': 'קבל הצעת מחיר'
    },
    'ru': {
        'title': 'Brick Development | Главный подрядчик',
        'hero': 'Строим будущее Ванкувера',
        'subhero': 'Лицензированный подрядчик Британской Колумбии',
        'desc': 'Ведущий генеральный подрядчик, специализирующийся на новых постройках, коммерческих помещениях и крупных ремонтах',
        'btn': 'Получить смету'
    },
    'uk': {
        'title': 'Brick Development | Головний підрядник',
        'hero': 'Будуємо майбутнє Ванкувера',
        'subhero': 'Ліцензований підрядник Британської Колумбії',
        'desc': 'Провідний генеральний підрядник, що спеціалізується на новобудовах, комерційних приміщеннях та капітальних ремонтах',
        'btn': 'Отримати кошторис'
    },
    'zh': {
        'title': 'Brick | 综合承包商',
        'hero': '建设温哥华的未来',
        'subhero': 'BC省许可承包商',
        'desc': '专长于新建工程及大型翻新工程',
        'btn': '获取报价'
    }
}

with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Add Google Maps SEO Schema to the root English file
if 'application/ld+json' not in template:
    maps_schema = '''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "GeneralContractor",
      "name": "Brick Development",
      "url": "https://YOUR_FUTURE_DOMAIN.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Vancouver",
        "addressRegion": "BC",
        "addressCountry": "CA"
      },
      "hasMap": "https://maps.google.com/?cid=YOUR_CID_HERE&hl=en"
    }
    </script>'''
    template = template.replace('</head>', f'{maps_schema}\n</head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template)

for lang_code, translations in languages.items():
    lang_dir = os.path.join(os.getcwd(), lang_code)
    if not os.path.exists(lang_dir):
        os.makedirs(lang_dir)
        
    html = template.replace('Brick Development | Vancouver General Contractor', translations['title'])
    html = html.replace("Building Vancouver's Future", translations['hero'])
    html = html.replace("BC Licensed General Contractor", translations['subhero'])
    html = html.replace("Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations", translations['desc'])
    html = html.replace("Get a Quote", translations['btn'])
    
    # Inject Localized Maps Schema
    localized_schema = f'''<script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "GeneralContractor",
      "name": "Brick Development",
      "url": "https://YOUR_FUTURE_DOMAIN.com/{lang_code}/",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Vancouver",
        "addressRegion": "BC",
        "addressCountry": "CA"
      }},
      "hasMap": "https://maps.google.com/?cid=YOUR_CID_HERE&hl={lang_code}"
    }}
    </script>'''
    
    # Replace the English schema we just added to the template with the localized one
    import re
    html = re.sub(r'<script type="application/ld\+json">.*?</script>', localized_schema, html, flags=re.DOTALL)
    
    with open(os.path.join(lang_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated " + lang_code)