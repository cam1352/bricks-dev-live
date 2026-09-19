import os
import re

# 1. Translate the remaining paragraphs and quotes
translations = {
    'fr': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': 'Entrepreneur général de premier plan spécialisé dans les nouvelles constructions, les espaces commerciaux et les rénovations majeures',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': 'Des maisons côtières de plusieurs millions de dollars aux espaces hôteliers haut de gamme, nous offrons un savoir-faire inégalé dans les secteurs commercial et résidentiel.',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': 'Bars sur mesure haut de gamme, cuisines commerciales et salles à manger atmosphériques conçues pour résister à un trafic intense tout en étant spectaculaires.',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': 'Rénovations de halls de luxe, réaménagements de suites d''invités et superbes espaces de patio extérieur qui rehaussent l''expérience des clients.',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': 'Aménagements de vente au détail chics et modernes et rénovations de cafés avec des comptoirs de qualité supérieure, des menuiseries sur mesure et des agencements accueillants.',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': 'Améliorations locatives à grande échelle, aménagements de bureaux modernes et finitions de salles de conférence exécutives.',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': 'Construction de A à Z de maisons côtières de luxe, avec une architecture moderne du nord-ouest du Pacifique et des intégrations fluides.',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': 'Ajouts structurels complets, modernisations extérieures et rénovations intérieures majeures pour les propriétés existantes.',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': 'Salles de bain de style spa et cuisines inspirées par des chefs, utilisant de la pierre importée, de la verrerie sur mesure et des accessoires haut de gamme.',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': 'Conception paysagère complète, murs de soutènement en béton architectural, pavage d''allées et installations de jardins.',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': 'Nous avons engagé Brick Development pour une rénovation complète de notre maison à Kitsilano. L''attention aux détails et le savoir-faire sont absolument inégalés. De vrais professionnels.',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': 'Notre construction sur mesure à Point Grey a été achevée à temps et exactement selon le budget. Ils ont rendu un projet complexe de plusieurs millions de dollars sans effort du début à la fin.',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': 'Absolument le meilleur entrepreneur général de Vancouver. Leur équipe de gestion de projet est phénoménale, et le résultat final a dépassé nos attentes les plus folles.',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': 'Qu''il s''agisse d''un espace de vente au détail commercial ou d''un domaine résidentiel sur mesure, Brick Development possède l''expertise pour lui donner vie.',
        'Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Coquitlam, Surrey, Langley, New Westminster': 'Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Coquitlam, Surrey, Langley, New Westminster'
    },
    'es': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': 'Contratista general de primer nivel especializado en nuevas construcciones, espacios comerciales y renovaciones importantes',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': 'Desde casas costeras multimillonarias hasta espacios de hospitalidad de alta gama, ofrecemos una artesanía incomparable tanto en el sector comercial como en el residencial.',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': 'Bares personalizados de alta gama, cocinas comerciales y comedores atmosféricos construidos para soportar un tráfico intenso sin dejar de lucir espectaculares.',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': 'Mejoras de vestíbulos de lujo, remodelaciones de suites de huéspedes y impresionantes espacios de patio al aire libre que elevan la experiencia del huésped.',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': 'Construcciones comerciales elegantes y modernas y renovaciones de cafés con encimeras de primera calidad, carpintería a medida y diseños acogedores.',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': 'Mejoras para inquilinos a gran escala, construcciones de oficinas modernas y acabados de salas de juntas ejecutivas.',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': 'Construcción desde cero de casas costeras de lujo, con arquitectura moderna del noroeste del Pacífico e integraciones perfectas.',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': 'Adiciones estructurales completas, modernizaciones exteriores y renovaciones interiores importantes para propiedades existentes.',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': 'Baños tipo spa y cocinas inspiradas en chefs que utilizan piedra importada, cristalería a medida y accesorios de alta gama.',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': 'Diseño de paisaje integral, muros de contención de hormigón arquitectónico, pavimentación de entradas de vehículos e instalaciones de jardines.',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': 'Contratamos a Brick Development para una renovación completa de nuestra casa en Kitsilano. La atención al detalle y la artesanía son absolutamente incomparables. Verdaderos profesionales.',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': 'Nuestra construcción personalizada en Point Grey se completó a tiempo y exactamente de acuerdo con el presupuesto. Hicieron que un proyecto complejo multimillonario pareciera fácil de principio a fin.',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': 'El mejor contratista general absoluto de Vancouver. Su equipo de gestión de proyectos es fenomenal y el resultado final superó nuestras expectativas más salvajes.',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': 'Ya sea un espacio comercial minorista o una propiedad residencial personalizada, Brick Development tiene la experiencia para darle vida.'
    },
    'zh': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': '一流的综合承包商，专长于新建工程、商业空间及大型翻新工程',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': '从数百万美元的沿海豪宅到高端酒店空间，我们在商业和住宅领域提供无与伦比的工艺。',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': '高端定制酒吧、商业厨房和极具氛围的餐厅，经久耐用，外观壮丽。',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': '豪华大堂升级、客房套房改造以及令人惊叹的户外露台空间，提升宾客体验。',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': '别致、现代的零售店面和咖啡馆翻新，配有优质台面、定制木制品和诱人的布局。',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': '全面的租户改善、现代办公空间建设和高管会议室装修。',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': '从零开始建造豪华沿海住宅，采用现代太平洋西北建筑风格和无缝连接。',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': '针对现有物业的全面结构扩建、外部现代化改造以及内部彻底翻新。',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': '如水疗中心般的浴室和受厨师启发的厨房，使用进口石材、定制玻璃制品和高端固定装置。',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': '全面的景观设计、建筑混凝土挡土墙、车道铺设和花园安装。',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': '我们聘请Brick Development对我们在Kitsilano的房子进行了彻底的翻新。其对细节的关注和工艺绝对是无与伦比的。真正的专业人士。',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': '我们在Point Grey的定制项目按时完成，且完全符合预算。他们让一个复杂的数百万美元项目从头到尾都感觉毫不费力。',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': '温哥华绝对最好的综合承包商。他们的项目管理团队非常出色，最终结果超出了我们最疯狂的期望。',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': '无论是商业零售空间还是定制住宅庄园，Brick Development都有将其变为现实的专业知识。'
    },
    'ru': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': 'Ведущий генеральный подрядчик, специализирующийся на новых постройках, коммерческих помещениях и крупных ремонтах',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': 'От многомиллионных прибрежных домов до элитных гостиничных пространств, мы предлагаем непревзойденное мастерство как в коммерческом, так и в жилом секторах.',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': 'Элитные бары на заказ, коммерческие кухни и атмосферные столовые, созданные для выдерживания высокой посещаемости и при этом выглядящие эффектно.',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': 'Модернизация роскошных вестибюлей, реконструкция гостевых номеров и потрясающие открытые патио, улучшающие впечатления гостей.',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': 'Шикарные, современные торговые павильоны и ремонт кафе с использованием высококачественных столешниц, столярных изделий на заказ и привлекательных планировок.',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': 'Полномасштабные улучшения для арендаторов, современные офисные помещения и отделка залов заседаний руководителей.',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': 'Строительство роскошных прибрежных домов с нуля, с современной архитектурой Тихоокеанского Северо-Запада и плавной интеграцией.',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': 'Полные структурные пристройки, внешняя модернизация и капитальный внутренний ремонт для существующих объектов недвижимости.',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': 'Ванные комнаты, похожие на спа, и кухни в стиле шеф-поваров с использованием импортного камня, изделий из стекла на заказ и высококачественной сантехники.',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': 'Комплексный ландшафтный дизайн, архитектурные бетонные подпорные стены, мощение подъездных путей и устройство садов.',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': 'Мы наняли Brick Development для капитального ремонта нашего дома в Кицилано. Внимание к деталям и мастерство абсолютно не имеют себе равных. Настоящие профессионалы.',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': 'Наш индивидуальный проект в Пойнт-Грей был завершен вовремя и точно в рамках бюджета. Они сделали сложный многомиллионный проект легким от начала до конца.',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': 'Абсолютно лучший генеральный подрядчик в Ванкувере. Их команда управления проектами феноменальна, а конечный результат превзошел наши самые смелые ожидания.',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': 'Будь то коммерческое торговое помещение или индивидуальная жилая усадьба, Brick Development обладает опытом, чтобы воплотить это в жизнь.'
    },
    'uk': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': 'Провідний генеральний підрядник, що спеціалізується на новобудовах, комерційних приміщеннях та капітальних ремонтах',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': 'Від багатомільйонних прибережних будинків до елітних готельних просторів, ми пропонуємо неперевершену майстерність як у комерційному, так і в житловому секторах.',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': 'Елітні бари на замовлення, комерційні кухні та атмосферні їдальні, створені для витримування високої відвідуваності і при цьому виглядають ефектно.',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': 'Модернізація розкішних вестибюлів, реконструкція гостьових номерів та приголомшливі відкриті патіо, що покращують враження гостей.',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': 'Шикарні, сучасні торгові павільйони та ремонт кафе з використанням високоякісних стільниць, столярних виробів на замовлення та привабливих планувань.',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': 'Повномасштабні покращення для орендарів, сучасні офісні приміщення та оздоблення залів засідань керівників.',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': 'Будівництво розкішних прибережних будинків з нуля, з сучасною архітектурою Тихоокеанського Північного Заходу та плавною інтеграцією.',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': 'Повні структурні прибудови, зовнішня модернізація та капітальний внутрішній ремонт для існуючих обєктів нерухомості.',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': 'Ванні кімнати, схожі на спа, та кухні в стилі шеф-кухарів з використанням імпортного каменю, виробів зі скла на замовлення та високоякісної сантехніки.',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': 'Комплексний ландшафтний дизайн, архітектурні бетонні підпірні стіни, мощення підїзних шляхів та влаштування садів.',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': 'Ми найняли Brick Development для капітального ремонту нашого будинку в Кітсілано. Увага до деталей і майстерність абсолютно не мають собі рівних. Справжні професіонали.',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': 'Наш індивідуальний проект у Пойнт-Грей був завершений вчасно і точно в рамках бюджету. Вони зробили складний багатомільйонний проект легким від початку до кінця.',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': 'Абсолютно найкращий генеральний підрядник у Ванкувері. Їхня команда управління проектами феноменальна, а кінцевий результат перевершив наші найсміливіші очікування.',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': 'Будь то комерційне торгове приміщення або індивідуальна житлова садиба, Brick Development має досвід, щоб втілити це в життя.'
    },
    'he': {
        'Premier General Contractor specializing in New Builds, Commercial Spaces & Major Renovations': 'קבלן ראשי מוביל המתמחה בבנייה חדשה, חללים מסחריים ושיפוצים גדולים',
        'From multi-million dollar coastal homes to high-end hospitality spaces, we deliver unparalleled craftsmanship across both commercial and residential sectors.': 'מבתי חוף של מיליוני דולרים ועד חללי אירוח יוקרתיים, אנו מספקים אומנות חסרת תקדים במגזר המסחרי והמגורים כאחד.',
        'High-end custom bars, commercial kitchens, and atmospheric dining rooms built to withstand heavy traffic while looking spectacular.': 'ברים יוקרתיים בהתאמה אישית, מטבחים מסחריים וחדרי אוכל אווירתיים שנבנו לעמוד בתנועה כבדה תוך שהם נראים מרהיבים.',
        'Luxury lobby upgrades, guest suite remodels, and stunning outdoor patio spaces that elevate the guest experience.': 'שדרוגי לובי יוקרתיים, שיפוץ סוויטות אורחים וחללי פטיו חיצוניים מדהימים המשדרגים את חווית האורח.',
        'Chic, modern retail build-outs and cafe renovations featuring premium countertops, custom millwork, and inviting layouts.': 'בניית קמעונאות מודרנית ושיקית ושיפוץ בתי קפה הכוללים משטחי פרימיום, עבודות עץ בהתאמה אישית ופריסות מזמינות.',
        'Full-scale tenant improvements, modern office build-outs, and executive boardroom finishings.': 'שיפורים בקנה מידה מלא לדיירים, בניית משרדים מודרנית וגימורי חדר ישיבות מנהלים.',
        'Ground-up construction of luxury coastal homes, featuring modern Pacific Northwest architecture and seamless integrations.': 'בנייה מהיסוד של בתי חוף יוקרתיים, הכוללים אדריכלות מודרנית של צפון מערב האוקיינוס השקט ושילובים חלקים.',
        'Complete structural additions, exterior modernizations, and major interior gut-renovations for existing properties.': 'תוספות מבניות שלמות, מודרניזציה חיצונית ושיפוצי פנים גדולים לנכסים קיימים.',
        'Spa-like bathroom retreats and chef-inspired kitchens utilizing imported stone, custom glasswork, and high-end fixtures.': 'חדרי רחצה דמויי ספא ומטבחים בהשראת שף המשתמשים באבן מיובאת, עבודות זכוכית בהתאמה אישית ואביזרי יוקרה.',
        'Comprehensive landscape design, architectural concrete retaining walls, driveway paving, and garden installations.': 'עיצוב נוף מקיף, קירות תמך מבטון אדריכלי, ריצוף שבילי גישה והתקנות גינות.',
        'We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.': 'שכרנו את Brick Development לשיפוץ פנימי מלא של הבית שלנו ב-Kitsilano. תשומת הלב לפרטים והאומנות היא ללא תחרות. מקצוענים אמיתיים.',
        'Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.': 'הבנייה המותאמת אישית שלנו ב-Point Grey הושלמה בזמן ובדיוק לתקציב. הם גרמו לפרויקט מורכב של מיליוני דולרים להרגיש חסר מאמץ מתחילתו ועד סופו.',
        'The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.': 'הקבלן הראשי הטוב ביותר בוונקובר. צוות ניהול הפרויקטים שלהם הוא פנומנלי, והתוצאה הסופית עלתה על הציפיות הפרועות ביותר שלנו.',
        'Whether it''s a commercial retail space or a custom residential estate, Brick Development has the expertise to bring it to life.': 'בין אם זה חלל קמעונאי מסחרי או אחוזה למגורים בהתאמה אישית, ל-Brick Development יש את המומחיות להחיות את זה.'
    }
}

for lang, dictionary in translations.items():
    filepath = os.path.join(lang, 'index.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # 1. Translate all paragraph content
        for en, translated in dictionary.items():
            html = html.replace(en, translated)
            
        # 2. Fix the dropdown 'selected' state for this specific language!
        # First remove any existing 'selected' attributes to ensure clean slate
        html = html.replace(' selected>', '>')
        
        # Now add the selected attribute ONLY to the correct option
        target_option = f'value="/bricks-dev-live/{lang}/index.html"'
        replacement_option = f'value="/bricks-dev-live/{lang}/index.html" selected'
        html = html.replace(target_option, replacement_option)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Translated all paragraphs and fixed dropdown selected states.")