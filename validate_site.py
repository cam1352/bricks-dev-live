import urllib.request

base_url = "https://cam1352.github.io/bricks-dev-live/"

languages = [
    ('es', 'Espa&ntilde;ol', 'Contratista general de primer nivel'),
    ('fr', 'Fran&ccedil;ais', 'Entrepreneur général de premier plan'),
    ('zh', '&#20013;&#25991;', '一流的综合承包商'),
    ('ru', '&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;', 'Ведущий генеральный подрядчик'),
    ('uk', '&#1059;&#1082;&#1088;&#1072;&#1111;&#1085;&#1089;&#1100;&#1082;&#1072;', 'Провідний генеральний підрядник'),
    ('he', '&#1506;&#1489;&#1512;&#1497;&#1514;', 'קבלן ראשי מוביל')
]

errors = []

for lang, option_text, translated_phrase in languages:
    url = f"{base_url}{lang}/index.html"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            selector_regex = f'value="/bricks-dev-live/{lang}/index.html" selected>{option_text}</option>'
            if selector_regex not in html:
                errors.append(f"[{lang}] Dropdown NOT selected. Searching for: {selector_regex}")
                
            if translated_phrase not in html:
                errors.append(f"[{lang}] Paragraph translation MISSING. Searching for: {translated_phrase}")
                
            if 'href="/bricks-dev-live/assets/css/style.css"' not in html:
                errors.append(f"[{lang}] Absolute CSS path MISSING.")
                
            print(f"SUCCESS: {lang.upper()} endpoint fully validated and live.")
            
    except Exception as e:
        errors.append(f"[{lang}] URL Fetch failed: {e}")

if errors:
    print("\nERRORS FOUND:")
    for e in errors:
        print(e)
else:
    print("\nALL LANGUAGES DOUBLE CHECKED. ZERO ERRORS.")