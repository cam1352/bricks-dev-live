import os

languages = {
    'es': {
        'title': 'Desarrollo Brick | Contratista General',
        'hero': 'Construyendo el futuro de Vancouver',
        'subhero': 'Contratista General',
        'desc': 'Especialistas en nuevas construcciones y renovaciones.',
        'btn': 'Obtener Presupuesto'
    },
    'fr': {
        'title': 'Brick | Entrepreneur Général',
        'hero': 'Construire l''avenir de Vancouver',
        'subhero': 'Entrepreneur général agréé',
        'desc': 'Spécialistes des nouvelles constructions.',
        'btn': 'Obtenir un Devis'
    },
    'zh': {
        'title': 'Brick | 综合承包商',
        'hero': '建设温哥华的未来',
        'subhero': 'BC省许可承包商',
        'desc': '专长于新建工程及大型翻新工程.',
        'btn': '获取报价'
    }
}

with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

for lang_code, translations in languages.items():
    lang_dir = os.path.join(os.getcwd(), lang_code)
    if not os.path.exists(lang_dir):
        os.makedirs(lang_dir)
        
    html = template.replace('Brick Development | Vancouver General Contractor', translations['title'])
    html = html.replace("Building Vancouver's Future", translations['hero'])
    html = html.replace("BC Licensed General Contractor", translations['subhero'])
    html = html.replace("Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations", translations['desc'])
    html = html.replace("Get a Quote", translations['btn'])
    
    with open(os.path.join(lang_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated " + lang_code)