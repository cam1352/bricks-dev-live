import os

translations = {
    'fr': {
        'Home': 'Accueil',
        'About': 'À propos',
        'Services': 'Services',
        'Projects': 'Projets',
        'Contact': 'Contact',
        'Call Today': 'Appelez aujourd''hui',
        'Our Services': 'Nos Services',
        'Residential Construction': 'Construction Résidentielle',
        'Commercial & Hospitality': 'Commercial et Hôtellerie',
        'Custom Home Builds': 'Maisons sur Mesure',
        'Kitchen & Bath Remodels': 'Rénovation Cuisine et Bain',
        'Whole-Home Renovations': 'Rénovations Complètes',
        'Luxury Landscaping': 'Aménagement Paysager de Luxe',
        'Restaurant & Bar Renovations': 'Rénovations de Restaurants et Bars',
        'Hotel & Resort Renovations': 'Rénovations d''Hôtels et de Complexes',
        'Cafe & Boutique Renovations': 'Rénovations de Cafés et Boutiques',
        'Commercial Improvements': 'Améliorations Commerciales',
        'Our Process': 'Notre Processus',
        'Design & Planning': 'Conception et Planification',
        'Construction': 'Construction',
        'Final Handover': 'Remise Finale',
        'Client Testimonials': 'Témoignages de Clients',
        'Ready to Build?': 'Prêt à Construire ?',
        'Discuss Your Project': 'Discutez de Votre Projet',
        'Proudly Servicing Vancouver': 'Fier de Servir Vancouver',
        'Construction Insights': 'Aperçus de Construction',
        'Frequently Asked Questions': 'Foire Aux Questions'
    },
    'es': {
        'Home': 'Inicio',
        'About': 'Nosotros',
        'Services': 'Servicios',
        'Projects': 'Proyectos',
        'Contact': 'Contacto',
        'Call Today': 'Llame Hoy',
        'Our Services': 'Nuestros Servicios',
        'Residential Construction': 'Construcción Residencial',
        'Commercial & Hospitality': 'Comercial y Hospitalidad',
        'Custom Home Builds': 'Casas a Medida',
        'Kitchen & Bath Remodels': 'Remodelación de Cocina y Baño',
        'Whole-Home Renovations': 'Renovaciones Completas',
        'Luxury Landscaping': 'Paisajismo de Lujo',
        'Restaurant & Bar Renovations': 'Renovaciones de Restaurantes y Bares',
        'Hotel & Resort Renovations': 'Renovaciones de Hoteles',
        'Cafe & Boutique Renovations': 'Renovaciones de Cafeterías',
        'Commercial Improvements': 'Mejoras Comerciales',
        'Our Process': 'Nuestro Proceso',
        'Design & Planning': 'Diseño y Planificación',
        'Construction': 'Construcción',
        'Final Handover': 'Entrega Final',
        'Client Testimonials': 'Testimonios de Clientes',
        'Ready to Build?': '¿Listo para Construir?',
        'Discuss Your Project': 'Discuta su Proyecto',
        'Proudly Servicing Vancouver': 'Sirviendo a Vancouver con Orgullo',
        'Construction Insights': 'Perspectivas de Construcción',
        'Frequently Asked Questions': 'Preguntas Frecuentes'
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

print("Translated UI elements for French and Spanish.")