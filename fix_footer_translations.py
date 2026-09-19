import os
import re

translations = {
    'fr': {
        'Read Our Blog (100+ Articles)': 'Lisez notre Blog (100+ Articles)',
        'Frequently Asked Questions': 'Foire Aux Questions',
        'Resources': 'Ressources',
        'About Our Company': 'À propos de notre entreprise',
        'Get a Quote': 'Obtenir un Devis'
    },
    'es': {
        'Read Our Blog (100+ Articles)': 'Lea nuestro Blog (100+ Artículos)',
        'Frequently Asked Questions': 'Preguntas Frecuentes',
        'Resources': 'Recursos',
        'About Our Company': 'Sobre Nuestra Empresa',
        'Get a Quote': 'Obtener Cotización'
    },
    'zh': {
        'Read Our Blog (100+ Articles)': '阅读我们的博客 (100+ 篇文章)',
        'Frequently Asked Questions': '常见问题',
        'Resources': '资源',
        'About Our Company': '关于我们公司',
        'Get a Quote': '获取报价'
    },
    'ru': {
        'Read Our Blog (100+ Articles)': 'Читайте наш блог (100+ статей)',
        'Frequently Asked Questions': 'Часто задаваемые вопросы',
        'Resources': 'Ресурсы',
        'About Our Company': 'О нашей компании',
        'Get a Quote': 'Получить смету'
    },
    'uk': {
        'Read Our Blog (100+ Articles)': 'Читайте наш блог (100+ статей)',
        'Frequently Asked Questions': 'Часті питання',
        'Resources': 'Ресурси',
        'About Our Company': 'Про нашу компанію',
        'Get a Quote': 'Отримати кошторис'
    },
    'he': {
        'Read Our Blog (100+ Articles)': 'קרא את הבלוג שלנו (100+ מאמרים)',
        'Frequently Asked Questions': 'שאלות נפוצות',
        'Resources': 'משאבים',
        'About Our Company': 'על החברה שלנו',
        'Get a Quote': 'קבל הצעת מחיר'
    }
}

for lang, dictionary in translations.items():
    filepath = os.path.join(lang, 'index.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        for en, translated in dictionary.items():
            html = html.replace(en, translated)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Translated the footer links properly.")