import os

translations = {
    'fr': {
        'Home': 'Accueil', 'About': 'À propos', 'Services': 'Services', 'Projects': 'Projets', 'Contact': 'Contact',
        'Call Today': 'Appelez aujourd''hui', 'Our Services': 'Nos Services', 'Ready to Build?': 'Prêt à Construire ?',
        'Residential Construction': 'Construction Résidentielle', 'Commercial & Hospitality': 'Commercial et Hôtellerie',
        'Custom Home Builds': 'Maisons sur Mesure', 'Kitchen & Bath Remodels': 'Rénovation Cuisine et Bain',
        'Whole-Home Renovations': 'Rénovations Complètes', 'Luxury Landscaping': 'Aménagement Paysager de Luxe',
        'Restaurant & Bar Renovations': 'Rénovations de Restaurants et Bars', 'Hotel & Resort Renovations': 'Rénovations d''Hôtels',
        'Cafe & Boutique Renovations': 'Rénovations de Cafés', 'Commercial Improvements': 'Améliorations Commerciales',
        'Our Process': 'Notre Processus', 'Design & Planning': 'Conception et Planification', 'Construction': 'Construction',
        'Final Handover': 'Remise Finale', 'Client Testimonials': 'Témoignages de Clients', 'Discuss Your Project': 'Discutez de Votre Projet',
        'Proudly Servicing Vancouver': 'Fier de Servir Vancouver', 'Resources': 'Ressources',
        'Read Our Blog': 'Lisez notre Blog', 'Frequently Asked Questions': 'Foire Aux Questions',
        'Get a Quote': 'Obtenir un Devis', 'About Our Company': 'À propos de notre entreprise'
    },
    'es': {
        'Home': 'Inicio', 'About': 'Nosotros', 'Services': 'Servicios', 'Projects': 'Proyectos', 'Contact': 'Contacto',
        'Call Today': 'Llame Hoy', 'Our Services': 'Nuestros Servicios', 'Ready to Build?': '¿Listo para Construir?',
        'Residential Construction': 'Construcción Residencial', 'Commercial & Hospitality': 'Comercial y Hospitalidad',
        'Custom Home Builds': 'Casas a Medida', 'Kitchen & Bath Remodels': 'Remodelación de Cocinas y Baños',
        'Whole-Home Renovations': 'Renovaciones Completas', 'Luxury Landscaping': 'Paisajismo de Lujo',
        'Restaurant & Bar Renovations': 'Renovaciones de Restaurantes', 'Hotel & Resort Renovations': 'Renovaciones de Hoteles',
        'Cafe & Boutique Renovations': 'Renovaciones de Cafeterías', 'Commercial Improvements': 'Mejoras Comerciales',
        'Our Process': 'Nuestro Proceso', 'Design & Planning': 'Diseño y Planificación', 'Construction': 'Construcción',
        'Final Handover': 'Entrega Final', 'Client Testimonials': 'Testimonios de Clientes', 'Discuss Your Project': 'Discuta su Proyecto',
        'Proudly Servicing Vancouver': 'Sirviendo a Vancouver con Orgullo', 'Resources': 'Recursos',
        'Read Our Blog': 'Lea nuestro Blog', 'Frequently Asked Questions': 'Preguntas Frecuentes',
        'Get a Quote': 'Obtener Cotización', 'About Our Company': 'Sobre Nuestra Empresa'
    },
    'zh': {
        'Home': '首页', 'About': '关于我们', 'Services': '服务', 'Projects': '项目', 'Contact': '联系我们',
        'Call Today': '今天致电', 'Our Services': '我们的服务', 'Ready to Build?': '准备好建造了吗？',
        'Residential Construction': '住宅建设', 'Commercial & Hospitality': '商业与酒店',
        'Custom Home Builds': '定制住宅', 'Kitchen & Bath Remodels': '厨房和浴室改造',
        'Whole-Home Renovations': '全屋翻新', 'Luxury Landscaping': '豪华园林绿化',
        'Restaurant & Bar Renovations': '餐厅和酒吧翻新', 'Hotel & Resort Renovations': '酒店和度假村翻新',
        'Cafe & Boutique Renovations': '咖啡馆和精品店翻新', 'Commercial Improvements': '商业改善',
        'Our Process': '我们的流程', 'Design & Planning': '设计与规划', 'Construction': '建设',
        'Final Handover': '最终移交', 'Client Testimonials': '客户感言', 'Discuss Your Project': '讨论您的项目',
        'Proudly Servicing Vancouver': '自豪地服务温哥华', 'Resources': '资源',
        'Read Our Blog': '阅读我们的博客', 'Frequently Asked Questions': '常见问题',
        'Get a Quote': '获取报价', 'About Our Company': '关于我们公司'
    },
    'ru': {
        'Home': 'Главная', 'About': 'О нас', 'Services': 'Услуги', 'Projects': 'Проекты', 'Contact': 'Контакты',
        'Call Today': 'Звоните сегодня', 'Our Services': 'Наши Услуги', 'Ready to Build?': 'Готовы строить?',
        'Residential Construction': 'Жилое строительство', 'Commercial & Hospitality': 'Коммерция и Гостеприимство',
        'Custom Home Builds': 'Дома на заказ', 'Kitchen & Bath Remodels': 'Ремонт кухонь и ванных',
        'Whole-Home Renovations': 'Полный ремонт домов', 'Luxury Landscaping': 'Ландшафтный дизайн',
        'Restaurant & Bar Renovations': 'Ремонт ресторанов и баров', 'Hotel & Resort Renovations': 'Ремонт гостиниц',
        'Cafe & Boutique Renovations': 'Ремонт кафе и бутиков', 'Commercial Improvements': 'Коммерческие улучшения',
        'Our Process': 'Наш Процесс', 'Design & Planning': 'Проектирование и Планирование', 'Construction': 'Строительство',
        'Final Handover': 'Сдача объекта', 'Client Testimonials': 'Отзывы клиентов', 'Discuss Your Project': 'Обсудить ваш проект',
        'Proudly Servicing Vancouver': 'С гордостью обслуживаем Ванкувер', 'Resources': 'Ресурсы',
        'Read Our Blog': 'Читайте наш блог', 'Frequently Asked Questions': 'Часто задаваемые вопросы',
        'Get a Quote': 'Получить смету', 'About Our Company': 'О нашей компании'
    },
    'uk': {
        'Home': 'Головна', 'About': 'Про нас', 'Services': 'Послуги', 'Projects': 'Проекти', 'Contact': 'Контакти',
        'Call Today': 'Телефонуйте сьогодні', 'Our Services': 'Наші Послуги', 'Ready to Build?': 'Готові будувати?',
        'Residential Construction': 'Житлове будівництво', 'Commercial & Hospitality': 'Комерція та Гостинність',
        'Custom Home Builds': 'Будинки на замовлення', 'Kitchen & Bath Remodels': 'Ремонт кухонь та ванних',
        'Whole-Home Renovations': 'Повний ремонт будинків', 'Luxury Landscaping': 'Ландшафтний дизайн',
        'Restaurant & Bar Renovations': 'Ремонт ресторанів та барів', 'Hotel & Resort Renovations': 'Ремонт готелів',
        'Cafe & Boutique Renovations': 'Ремонт кафе та бутиків', 'Commercial Improvements': 'Комерційні покращення',
        'Our Process': 'Наш Процес', 'Design & Planning': 'Проектування та Планування', 'Construction': 'Будівництво',
        'Final Handover': 'Здача обєкта', 'Client Testimonials': 'Відгуки клієнтів', 'Discuss Your Project': 'Обговорити ваш проект',
        'Proudly Servicing Vancouver': 'З гордістю обслуговуємо Ванкувер', 'Resources': 'Ресурси',
        'Read Our Blog': 'Читайте наш блог', 'Frequently Asked Questions': 'Часті питання',
        'Get a Quote': 'Отримати кошторис', 'About Our Company': 'Про нашу компанію'
    },
    'he': {
        'Home': 'בית', 'About': 'אודות', 'Services': 'שירותים', 'Projects': 'פרויקטים', 'Contact': 'צור קשר',
        'Call Today': 'התקשר היום', 'Our Services': 'השירותים שלנו', 'Ready to Build?': 'מוכן לבנות?',
        'Residential Construction': 'בנייה למגורים', 'Commercial & Hospitality': 'מסחר ומלונאות',
        'Custom Home Builds': 'בתים בהתאמה אישית', 'Kitchen & Bath Remodels': 'שיפוץ מטבחים וחדרי רחצה',
        'Whole-Home Renovations': 'שיפוץ בתים מלא', 'Luxury Landscaping': 'אדריכלות נוף יוקרתית',
        'Restaurant & Bar Renovations': 'שיפוץ מסעדות וברים', 'Hotel & Resort Renovations': 'שיפוץ מלונות',
        'Cafe & Boutique Renovations': 'שיפוץ בתי קפה ובוטיקים', 'Commercial Improvements': 'שיפורים מסחריים',
        'Our Process': 'התהליך שלנו', 'Design & Planning': 'עיצוב ותכנון', 'Construction': 'בנייה',
        'Final Handover': 'מסירה סופית', 'Client Testimonials': 'המלצות לקוחות', 'Discuss Your Project': 'שוחח על הפרויקט שלך',
        'Proudly Servicing Vancouver': 'משרתים בגאווה את ונקובר', 'Resources': 'משאבים',
        'Read Our Blog': 'קרא את הבלוג שלנו', 'Frequently Asked Questions': 'שאלות נפוצות',
        'Get a Quote': 'קבל הצעת מחיר', 'About Our Company': 'על החברה שלנו'
    }
}

for lang, dictionary in translations.items():
    filepath = os.path.join(lang, 'index.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Standardize HTML before replacing
        for en, translated in dictionary.items():
            html = html.replace(f">{en}<", f">{translated}<")
            # For attributes or loose text
            html = html.replace(f'"{en}"', f'"{translated}"')
            html = html.replace(f'{en}</a>', f'{translated}</a>')
            html = html.replace(f'{en}</p>', f'{translated}</p>')
            html = html.replace(f'{en}</h3>', f'{translated}</h3>')
            html = html.replace(f'{en}</h2>', f'{translated}</h2>')
            html = html.replace(f'{en}</h1>', f'{translated}</h1>')
            html = html.replace(f'{en}</li>', f'{translated}</li>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Deeply translated the site text for all 6 languages.")