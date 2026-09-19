import os

langs = {
    'fr': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', 'Des maisons sur mesure aux propriétés commerciales, nous donnons vie à votre vision avec précision et une qualité sans compromis.'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', 'Gestion de projet complète, de la planification initiale et des permis jusqu''à l''inspection finale et la remise.'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', 'Transformez votre espace existant avec nos services experts de rénovation majeure, d''extension et de remodelage.'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', 'Nous avons engagé Brick Development pour une rénovation complète de notre maison. L''attention aux détails est absolument inégalée. De vrais professionnels.'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', 'Notre construction sur mesure a été achevée à temps et exactement selon le budget. Un projet complexe rendu sans effort du début à la fin.'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', 'Absolument le meilleur entrepreneur général de Vancouver. Leur équipe de gestion est phénoménale, et le résultat final a dépassé nos attentes.')
    ],
    'es': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', 'Desde casas a medida hasta propiedades comerciales, damos vida a su visión con precisión y calidad intransigente.'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', 'Gestión integral de proyectos desde la planificación inicial y permisos hasta la inspección final y entrega.'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', 'Transforme su espacio existente con nuestros expertos servicios de renovación, extensión y remodelación.'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', 'Contratamos a Brick Development para una renovación completa de nuestra casa. La atención al detalle es absolutamente incomparable. Verdaderos profesionales.'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', 'Nuestra construcción a medida se completó a tiempo y exactamente al presupuesto. Un proyecto complejo sin esfuerzo de principio a fin.'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', 'El mejor contratista general absoluto de Vancouver. Su equipo de gestión es fenomenal, y el resultado final superó nuestras expectativas.')
    ],
    'zh': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', '从定制住宅到商业地产，我们以精准和毫不妥协的质量将您的愿景变为现实。'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', '全面的项目管理，从最初的规划和许可到最终的检查和移交。'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', '通过我们专业的重大翻新、扩建和改造服务，改变您现有的空间。'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', '我们聘请了Brick Development对我们的房子进行了彻底的翻新。对细节的关注绝对是无与伦比的。真正的专业人士。'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', '我们的定制建筑按时完成，完全符合预算。一个复杂的项目从头到尾都毫不费力。'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', '温哥华绝对最好的综合承包商。他们的管理团队非常出色，最终结果超出了我们的预期。')
    ],
    'ru': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', 'От домов на заказ до коммерческой недвижимости, мы воплощаем ваше видедение в жизнь с точностью и бескомпромиссным качеством.'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', 'Комплексное управление проектом от первоначального планирования и разрешений до окончательной проверки и сдачи.'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', 'Преобразите ваше существующее пространство с нашими экспертными услугами по капитальному ремонту, расширению и реконструкции.'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', 'Мы наняли Brick Development для полного ремонта нашего дома. Внимание к деталям абсолютно непревзойденное. Настоящие профессионалы.'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', 'Наш индивидуальный проект был завершен в срок и точно в рамках бюджета. Сложный проект был реализован без усилий от начала до конца.'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', 'Абсолютно лучший генеральный подрядчик в Ванкувере. Их команда менеджеров феноменальна, а результат превзошел наши ожидания.')
    ],
    'uk': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', 'Від будинків на замовлення до комерційної нерухомості, ми втілюємо ваше бачення в життя з точністю та безкомпромісною якістю.'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', 'Комплексне управління проектом від початкового планування та дозволів до остаточної перевірки та здачі.'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', 'Перетворіть ваш існуючий простір з нашими експертними послугами з капітального ремонту, розширення та реконструкції.'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', 'Ми найняли Brick Development для повного ремонту нашого будинку. Увага до деталей абсолютно неперевершена. Справжні професіонали.'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', 'Наш індивідуальний проект був завершений вчасно і точно в рамках бюджету. Складний проект був реалізований без зусиль від початку до кінця.'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', 'Абсолютно найкращий генеральний підрядник у Ванкувері. Їхня команда менеджерів феноменальна, а результат перевершив наші очікування.')
    ],
    'he': [
        ('From custom homes to commercial properties, we bring your vision to life with precision and uncompromising quality.', 'מבתים מותאמים אישית ועד לנכסים מסחריים, אנו מגשימים את החזון שלך בדיוק ובאיכות בלתי מתפשרת.'),
        ('Comprehensive project management from initial planning and permits to final inspection and handover.', 'ניהול פרויקטים מקיף מתכנון ראשוני והיתרים ועד לבדיקה סופית ומסירה.'),
        ('Transform your existing space with our expert major renovation, extension, and remodeling services.', 'שנה את החלל הקיים שלך עם שירותי השיפוץ, ההרחבה והעיצוב מחדש המומחים שלנו.'),
        ('We hired Brick Development for a full gut renovation of our Kitsilano home. The attention to detail and craftsmanship is absolutely unparalleled. True professionals.', 'שכרנו את Brick Development לשיפוץ מלא של הבית שלנו. תשומת הלב לפרטים היא ללא תחרות. מקצוענים אמיתיים.'),
        ('Our custom build in Point Grey was completed on time and exactly to budget. They made a complex, multi-million dollar project feel effortless from start to finish.', 'הבנייה המותאמת אישית שלנו הושלמה בזמן ובדיוק לתקציב. פרויקט מורכב בוצע ללא מאמץ מתחילתו ועד סופו.'),
        ('The absolute best general contractor in Vancouver. Their project management team is phenomenal, and the final result exceeded our wildest expectations.', 'הקבלן הראשי הטוב ביותר בוונקובר. צוות הניהול שלהם פנומנלי, והתוצאה עלתה על הציפיות שלנו.')
    ]
}

for lang, phrases in langs.items():
    filepath = os.path.join(lang, 'index.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        for en, translated in phrases:
            # Replace ignoring extra spaces/newlines that might be in html
            import re
            pattern = re.compile(re.escape(en).replace(r'\ ', r'\s+'), re.DOTALL)
            html = pattern.sub(translated, html)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Correctly translated the index paragraphs.")