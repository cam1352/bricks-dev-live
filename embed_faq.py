import os
import re

faqs = {
    'en': {
        'title': 'Frequently Asked Questions',
        'q1': 'How much does a custom home cost?', 'a1': 'Costs vary depending on materials and square footage, but typically range from  to + per square foot in Vancouver.',
        'q2': 'Do you handle building permits?', 'a2': 'Yes, we handle the entire permitting process with the City of Vancouver and surrounding municipalities.',
        'q3': 'Are you WorkSafeBC licensed?', 'a3': 'Absolutely. We are fully licensed, insured, and WorkSafeBC compliant.'
    },
    'es': {
        'title': 'Preguntas Frecuentes',
        'q1': '¿Cuánto cuesta una casa a medida?', 'a1': 'Los costos varían según los materiales y los metros cuadrados, pero normalmente oscilan entre  y + por pie cuadrado en Vancouver.',
        'q2': '¿Se encargan de los permisos de construcción?', 'a2': 'Sí, manejamos todo el proceso de permisos con la ciudad de Vancouver y los municipios circundantes.',
        'q3': '¿Tienen licencia de WorkSafeBC?', 'a3': 'Absolutamente. Estamos totalmente autorizados, asegurados y cumplimos con WorkSafeBC.'
    },
    'fr': {
        'title': 'Foire Aux Questions',
        'q1': 'Combien coûte une maison sur mesure ?', 'a1': 'Les coûts varient en fonction des matériaux et de la superficie, mais se situent généralement entre 350 $ et 600 $ et plus par pied carré à Vancouver.',
        'q2': 'Gérez-vous les permis de construire ?', 'a2': 'Oui, nous gérons l''ensemble du processus de permis avec la ville de Vancouver et les municipalités environnantes.',
        'q3': 'Êtes-vous titulaire d''une licence WorkSafeBC ?', 'a3': 'Absolument. Nous sommes entièrement agréés, assurés et conformes à WorkSafeBC.'
    },
    'zh': {
        'title': '常见问题',
        'q1': '定制房屋的成本是多少？', 'a1': '成本因材料和面积而异，但在温哥华通常在每平方英尺350到600美元以上。',
        'q2': '你们处理建筑许可证吗？', 'a2': '是的，我们负责与温哥华市及周边城市的整个许可流程。',
        'q3': '你们有WorkSafeBC的许可吗？', 'a3': '绝对有。我们拥有完全的许可、保险，并符合WorkSafeBC的规定。'
    },
    'ru': {
        'title': 'Часто задаваемые вопросы',
        'q1': 'Сколько стоит дом на заказ?', 'a1': 'Стоимость зависит от материалов и площади, но обычно составляет от  до + за квадратный фут в Ванкувере.',
        'q2': 'Вы занимаетесь разрешениями на строительство?', 'a2': 'Да, мы берем на себя весь процесс получения разрешений в Ванкувере и близлежащих муниципалитетах.',
        'q3': 'У вас есть лицензия WorkSafeBC?', 'a3': 'Абсолютно. Мы полностью лицензированы, застрахованы и соблюдаем требования WorkSafeBC.'
    },
    'uk': {
        'title': 'Часті питання',
        'q1': 'Скільки коштує будинок на замовлення?', 'a1': 'Вартість залежить від матеріалів та площі, але зазвичай становить від  до + за квадратний фут у Ванкувері.',
        'q2': 'Ви займаєтесь дозволами на будівництво?', 'a2': 'Так, ми беремо на себе весь процес отримання дозволів у Ванкувері та прилеглих муніципалітетах.',
        'q3': 'У вас є ліцензія WorkSafeBC?', 'a3': 'Абсолютно. Ми повністю ліцензовані, застраховані та дотримуємося вимог WorkSafeBC.'
    },
    'he': {
        'title': 'שאלות נפוצות',
        'q1': 'כמה עולה בית בהתאמה אישית?', 'a1': 'העלויות משתנות בהתאם לחומרים ולגודל, אך בדרך כלל נעות בין  ל-+ לכל רגל מרובע בוונקובר.',
        'q2': 'האם אתם מטפלים בהיתרי בנייה?', 'a2': 'כן, אנו מטפלים בכל תהליך ההיתרים מול עיריית ונקובר והעיריות הסמוכות.',
        'q3': 'האם יש לכם רישיון WorkSafeBC?', 'a3': 'בהחלט. אנו מורשים לחלוטין, מבוטחים ועומדים בתקני WorkSafeBC.'
    }
}

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.netlify' in root: continue
    
    # Determine language
    lang = 'en'
    dirname = os.path.basename(root)
    if dirname in faqs.keys():
        lang = dirname
        
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # 1. Remove FAQ link from Footer
            content = re.sub(r'<li><a href="/bricks-dev-live/faq.html".*?</a></li>', '', content)
            
            # 2. Inject FAQ section into index.html right before footer
            if file == 'index.html':
                # Check if FAQ is already injected to avoid duplicates
                if 'id="faq"' not in content:
                    f_data = faqs[lang]
                    faq_html = f'''
        <section class="container fade-in" id="faq" style="margin-top: 60px; margin-bottom: 60px;">
            <h2 style="color: var(--primary); border-bottom: 2px solid var(--secondary); padding-bottom: 10px;">{f_data['title']}</h2>
            <div style="margin-top: 20px;">
                <h4 style="color: var(--primary); margin-bottom: 5px;">{f_data['q1']}</h4>
                <p style="color: var(--text-light); margin-bottom: 15px;">{f_data['a1']}</p>
                
                <h4 style="color: var(--primary); margin-bottom: 5px;">{f_data['q2']}</h4>
                <p style="color: var(--text-light); margin-bottom: 15px;">{f_data['a2']}</p>

                <h4 style="color: var(--primary); margin-bottom: 5px;">{f_data['q3']}</h4>
                <p style="color: var(--text-light); margin-bottom: 15px;">{f_data['a3']}</p>
            </div>
        </section>
        <footer'''
                    content = content.replace('<footer', faq_html)
                    
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Embedded FAQ natively on the homepage and removed the separate FAQ link.")